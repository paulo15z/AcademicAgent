"""
Configuration and fixtures for database tests.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.academic_agent.database.models import Base
from src.academic_agent.database.database import SessionLocal

# Use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """
    Pytest fixture to create a new database session for each test.
    
    Creates all tables, yields a session, and then drops all tables after the test.
    """
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Drop all tables after the test is done
        Base.metadata.drop_all(bind=engine) 