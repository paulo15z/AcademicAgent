"""
Workflow for summarizing academic content from the database.
"""
from openai import OpenAI
from sqlalchemy.orm import Session

from ..database import crud
from ..validation import schemas


def run_summarization_workflow(
    client: OpenAI, db: Session, params: schemas.SummarizationWorkflowParams
) -> str:
    """
    Runs the summarization workflow on a document from the database.

    Args:
        client (OpenAI): The OpenAI client instance.
        db (Session): The database session.
        params (schemas.SummarizationWorkflowParams): The parameters for the workflow.

    Returns:
        str: The generated summary.

    Raises:
        ValueError: If the document is not found or the API response is invalid.
    """
    document = crud.get_document(db, document_id=params.document_id)
    if not document:
        raise ValueError(f"Document with ID {params.document_id} not found.")

    text_to_summarize = document.content
    if not text_to_summarize.strip():
        return "The document is empty and cannot be summarized."

    system_prompt = (
        "Você é um assistente de pesquisa acadêmica especializado em sintetizar informações. "
        "Sua tarefa é criar um resumo conciso e claro do texto fornecido, destacando os "
        "principais argumentos, metodologias e conclusões."
    )

    response = client.chat.completions.create(
        model=params.model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_to_summarize},
        ],
        temperature=0.5,
        max_tokens=500,  # Keeping max_tokens to manage cost and response size
    )
    
    summary = response.choices[0].message.content
    if not summary:
        raise ValueError("Failed to get a valid summary from the API.")
        
    return summary.strip() 