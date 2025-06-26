"""
Tests for CRUD operations.
"""

from sqlalchemy.orm import Session
from src.academic_agent.database import crud
from src.academic_agent.validation import schemas

def test_create_and_get_document(db_session: Session):
    """
    Test creating a document and then retrieving it.
    """
    doc_in = schemas.DocumentCreate(
        title="Test Document",
        source="local",
        content="This is the content of the test document."
    )
    
    # Create document
    created_doc = crud.create_document(db=db_session, document=doc_in)
    assert created_doc.id is not None
    assert created_doc.title == doc_in.title
    assert created_doc.content == doc_in.content

    # Get document
    retrieved_doc = crud.get_document(db=db_session, document_id=created_doc.id)
    assert retrieved_doc is not None
    assert retrieved_doc.id == created_doc.id
    assert retrieved_doc.title == created_doc.title

def test_get_nonexistent_document(db_session: Session):
    """
    Test that retrieving a non-existent document returns None.
    """
    retrieved_doc = crud.get_document(db=db_session, document_id=999)
    assert retrieved_doc is None

def test_get_multiple_documents(db_session: Session):
    """
    Test retrieving a list of documents with pagination.
    """
    # Create multiple documents
    crud.create_document(db=db_session, document=schemas.DocumentCreate(title="Doc 1", content="..."))
    crud.create_document(db=db_session, document=schemas.DocumentCreate(title="Doc 2", content="..."))
    
    # Get all documents
    docs = crud.get_documents(db=db_session)
    assert len(docs) == 2
    assert docs[0].title == "Doc 1"

    # Test pagination
    docs_limit_1 = crud.get_documents(db=db_session, skip=0, limit=1)
    assert len(docs_limit_1) == 1
    assert docs_limit_1[0].title == "Doc 1"

    docs_skip_1 = crud.get_documents(db=db_session, skip=1, limit=1)
    assert len(docs_skip_1) == 1
    assert docs_skip_1[0].title == "Doc 2"

def test_create_and_get_chunks(db_session: Session):
    """
    Test creating text chunks for a document and retrieving them.
    """
    # First, create a parent document
    doc_in = schemas.DocumentCreate(title="Parent Document", content="...")
    parent_doc = crud.create_document(db=db_session, document=doc_in)

    # Create chunks for the document
    chunk1_in = schemas.TextChunkCreate(content="First chunk.")
    chunk2_in = schemas.TextChunkCreate(content="Second chunk.")
    crud.create_text_chunk(db=db_session, chunk=chunk1_in, document_id=parent_doc.id)
    crud.create_text_chunk(db=db_session, chunk=chunk2_in, document_id=parent_doc.id)

    # Get chunks for the document
    chunks = crud.get_text_chunks_by_document(db=db_session, document_id=parent_doc.id)
    assert len(chunks) == 2
    assert chunks[0].content == chunk1_in.content
    assert chunks[1].content == chunk2_in.content 