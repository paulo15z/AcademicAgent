"""
Database models for the Academic Agent.
"""

from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Document(Base):
    """
    Represents a single academic document stored in the database.
    
    This could be an article, a chapter, or any piece of text that the user ingests.
    """
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    source = Column(String(255))  # e.g., file path, URL
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationship to text chunks
    chunks = relationship("TextChunk", back_populates="document")

    def __repr__(self):
        return f"<Document(id={self.id}, title='{self.title}')>"

class TextChunk(Base):
    """
    Represents a smaller chunk of a larger document.
    
    Breaking down large documents into smaller chunks is essential for processing
    with LLMs that have context window limitations.
    """
    __tablename__ = "text_chunks"

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(Text) # In the future, this will store vector embeddings for similarity search
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationship back to the parent document
    document = relationship("Document", back_populates="chunks")

    def __repr__(self):
        return f"<TextChunk(id={self.id}, document_id={self.document_id})>" 