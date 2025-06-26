"""
Unit tests for the summarization workflow.
"""
import pytest
from unittest.mock import MagicMock
from openai import OpenAI, APIError
from src.academic_agent.workflows.summarization_workflow import run_summarization_workflow

@pytest.fixture
def mock_openai_client():
    """Fixture to create a mock OpenAI client."""
    return MagicMock(spec=OpenAI)

def test_run_summarization_workflow_success(mock_openai_client):
    """
    Tests the successful execution of the summarization workflow.
    """
    # Arrange
    params = {"text": "Este é um longo texto para ser resumido."}
    expected_summary = "Este é o resumo."

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = expected_summary
    mock_openai_client.chat.completions.create.return_value = mock_response

    # Act
    result = run_summarization_workflow(mock_openai_client, params)

    # Assert
    assert result == expected_summary
    mock_openai_client.chat.completions.create.assert_called_once()
    _, call_kwargs = mock_openai_client.chat.completions.create.call_args
    assert call_kwargs["messages"][1]["content"] == params["text"]

def test_run_summarization_workflow_missing_text(mock_openai_client):
    """
    Tests that the workflow raises a ValueError if the 'text' parameter is missing.
    """
    with pytest.raises(ValueError, match="The 'text' parameter is required for the summarization workflow."):
        run_summarization_workflow(mock_openai_client, {})

def test_run_summarization_workflow_api_failure(mock_openai_client):
    """
    Tests that the workflow raises an error if the API call fails.
    """
    params = {"text": "Um texto qualquer."}
    mock_openai_client.chat.completions.create.side_effect = APIError("API Error", request=MagicMock(), body=None)

    with pytest.raises(ValueError, match="Failed to generate summary due to an API error."):
        run_summarization_workflow(mock_openai_client, params)

def test_run_summarization_workflow_empty_response(mock_openai_client):
    """
    Tests that the workflow raises a ValueError if the API returns an empty response.
    """
    params = {"text": "Outro texto."}
    
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = ""
    mock_openai_client.chat.completions.create.return_value = mock_response

    with pytest.raises(ValueError, match="Failed to get a valid summary from the API."):
        run_summarization_workflow(mock_openai_client, params) 