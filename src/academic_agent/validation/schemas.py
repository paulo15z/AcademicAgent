"""
Pydantic schemas for data validation.
"""

from pydantic import BaseModel
import datetime
from typing import List, Optional

# --- TextChunk Schemas ---

class TextChunkBase(BaseModel):
    content: str
    
class TextChunkCreate(TextChunkBase):
    pass

class TextChunk(TextChunkBase):
    id: int
    document_id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True

# --- Document Schemas ---

class DocumentBase(BaseModel):
    title: str
    source: Optional[str] = None
    content: str

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: int
    created_at: datetime.datetime
    chunks: List[TextChunk] = []

    class Config:
        from_attributes = True

# --- Workflow Schemas ---

class ABNTWorkflowParams(BaseModel):
    """Parameters for the ABNT formatting workflow."""
    file_path: str
    model_name: str = "gpt-4.1-nano"

class ABNTWorkflowResponse(BaseModel):
    """Response model for the ABNT formatting workflow."""
    formatted_text: str

class SummarizationWorkflowParams(BaseModel):
    """Parameters for the summarization workflow."""
    document_id: int
    model_name: str = "gpt-4.1-nano"

class SummarizationWorkflowResponse(BaseModel):
    """Response model for the summarization workflow."""
    summary: str 