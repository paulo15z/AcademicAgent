import os
import shutil
import tempfile
from contextlib import asynccontextmanager

from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from openai import OpenAI
from sqlalchemy.orm import Session

from academic_agent.database import crud, database
from academic_agent.validation import schemas
from academic_agent.workflows import abnt_workflow, summarization_workflow
from academic_agent.utils.file_parser import read_text_from_file


# --- App Lifespan ---

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown events.
    """
    print("Starting up...")
    database.init_db()
    yield
    print("Shutting down...")


# --- App Initialization ---

app = FastAPI(
    title="AI Academic Agent",
    description="An AI-powered agent for academic tasks.",
    lifespan=lifespan,
)

# --- Dependencies ---

def get_db_session():
    """Dependency to get a database session."""
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize OpenAI client
# Make sure to set the OPENAI_API_KEY environment variable
try:
    client = OpenAI()
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    client = None


# --- API Endpoints ---

@app.get("/")
def read_root():
    """Root endpoint to check if the API is running."""
    return {"message": "Welcome to the AI Academic Agent API"}


@app.post("/format-abnt/", response_model=schemas.ABNTWorkflowResponse)
def format_abnt_endpoint(
    file: UploadFile = File(...),
):
    """
    Receives a file, formats its content according to ABNT standards,
    and returns the formatted text.
    """
    if not client:
        raise HTTPException(status_code=500, detail="OpenAI client not initialized. Check API key.")
        
    # The ABNT workflow expects a file path, so we save the uploaded file temporarily
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        
        params = schemas.ABNTWorkflowParams(file_path=tmp_path)
        formatted_text = abnt_workflow.run_abnt_workflow(client, params)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    finally:
        # Clean up the temporary file
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.remove(tmp_path)

    return {"formatted_text": formatted_text}


@app.post("/documents/", response_model=schemas.Document)
def ingest_document_endpoint(
    file: UploadFile = File(...),
    db: Session = Depends(get_db_session),
):
    """
    Receives a file, extracts its content, and saves it as a new
    document in the database.
    """
    try:
        # Save uploaded file to a temporary path to be read
        with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        # Extract text using the centralized parser
        content = read_text_from_file(tmp_path)

        # Create document schema and save to DB
        document_in = schemas.DocumentCreate(
            title=file.filename or "Untitled",
            source=f"upload:{file.filename}",
            content=content
        )
        db_document = crud.create_document(db=db, document=document_in)

        # Split content into chunks and save them
        chunks = content.split('\n\n')
        for chunk_content in chunks:
            if chunk_content.strip():  # Ensure chunk is not just whitespace
                chunk_schema = schemas.TextChunkCreate(content=chunk_content)
                crud.create_text_chunk(db=db, chunk=chunk_schema, document_id=db_document.id)  # type: ignore

        db.refresh(db_document)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during ingestion: {str(e)}")
    finally:
        # Clean up the temporary file
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.remove(tmp_path)

    return db_document


@app.post("/summarize/", response_model=schemas.SummarizationWorkflowResponse)
def summarize_document_endpoint(
    params: schemas.SummarizationWorkflowParams,
    db: Session = Depends(get_db_session),
):
    """
    Summarizes the content of a document stored in the database.
    """
    if not client:
        raise HTTPException(status_code=500, detail="OpenAI client not initialized. Check API key.")
    
    try:
        summary = summarization_workflow.run_summarization_workflow(
            client=client, db=db, params=params
        )
    except ValueError as e:
        # If the document is not found, it will raise a ValueError.
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

    return {"summary": summary} 