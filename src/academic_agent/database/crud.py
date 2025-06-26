"""
CRUD (Create, Read, Update, Delete) operations for the database.
"""

from sqlalchemy.orm import Session
from . import models
from ..validation import schemas

# --- Session Management ---

def get_db():
    """
    Dependency to get a database session.
    Ensures the session is closed after the request is finished.
    """
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Document Operations ---

def create_document(db: Session, document: schemas.DocumentCreate) -> models.Document:
    """
    Creates a new document in the database.

    Args:
        db (Session): The database session.
        document (schemas.DocumentCreate): The document data to create.

    Returns:
        models.Document: The newly created document object.
    """
    db_document = models.Document(
        title=document.title,
        source=document.source,
        content=document.content
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_document(db: Session, document_id: int) -> models.Document | None:
    """
    Retrieves a document by its ID.

    Args:
        db (Session): The database session.
        document_id (int): The ID of the document to retrieve.

    Returns:
        Optional[models.Document]: The document object if found, otherwise None.
    """
    return db.query(models.Document).filter(models.Document.id == document_id).first()

def get_documents(db: Session, skip: int = 0, limit: int = 100) -> list[models.Document]:
    """
    Retrieves a list of documents with pagination.

    Args:
        db (Session): The database session.
        skip (int): The number of records to skip.
        limit (int): The maximum number of records to return.

    Returns:
        List[models.Document]: A list of document objects.
    """
    return db.query(models.Document).offset(skip).limit(limit).all()

# --- TextChunk Operations ---

def get_text_chunks_by_document(db: Session, document_id: int) -> list[models.TextChunk]:
    """
    Retrieves all text chunks for a specific document.

    Args:
        db (Session): The database session.
        document_id (int): The ID of the parent document.

    Returns:
        List[models.TextChunk]: A list of text chunk objects.
    """
    return db.query(models.TextChunk).filter(models.TextChunk.document_id == document_id).all()

def create_text_chunk(db: Session, chunk: schemas.TextChunkCreate, document_id: int) -> models.TextChunk:
    """
    Creates a new text chunk associated with a document.

    Args:
        db (Session): The database session.
        chunk (schemas.TextChunkCreate): The chunk data to create.
        document_id (int): The ID of the parent document.

    Returns:
        models.TextChunk: The newly created text chunk object.
    """
    db_chunk = models.TextChunk(
        **chunk.model_dump(),
        document_id=document_id
    )
    db.add(db_chunk)
    db.commit()
    db.refresh(db_chunk)
    return db_chunk 