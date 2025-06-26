"""
Unit tests for the ABNT formatting workflow.
"""

import pytest
from unittest.mock import MagicMock, patch
from openai import OpenAI
from src.academic_agent.workflows.abnt_workflow import run_abnt_workflow


@pytest.fixture
def mock_openai_client():
    """Fixture to create a mock OpenAI client."""
    client = MagicMock(spec=OpenAI)
    client.chat = MagicMock()
    client.chat.completions = MagicMock()
    return client


@patch('src.academic_agent.workflows.abnt_workflow._read_text_from_file', return_value="Texto extraído do arquivo.")
def test_run_abnt_workflow_success(mock_read_file, mock_openai_client):
    """
    Tests the successful execution of the ABNT formatting workflow with a valid file path.
    """
    # Arrange
    params = {"file_path": "/fake/path/document.pdf"}
    expected_response = "Texto formatado."

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = expected_response
    mock_openai_client.chat.completions.create.return_value = mock_response

    # Act
    result = run_abnt_workflow(mock_openai_client, params)

    # Assert
    assert result == expected_response
    mock_read_file.assert_called_once_with(params["file_path"])
    mock_openai_client.chat.completions.create.assert_called_once()
    _, call_kwargs = mock_openai_client.chat.completions.create.call_args
    assert call_kwargs["messages"][1]["content"] == "Texto extraído do arquivo."


def test_run_abnt_workflow_missing_filepath_param(mock_openai_client):
    """
    Tests that the workflow raises a ValueError if 'file_path' parameter is missing.
    """
    with pytest.raises(ValueError, match="The 'file_path' parameter is required for ABNT formatting."):
        run_abnt_workflow(mock_openai_client, {"other_param": "value"})


@patch('src.academic_agent.workflows.abnt_workflow._read_text_from_file', side_effect=FileNotFoundError("File not found"))
def test_run_abnt_workflow_file_not_found(mock_read_file, mock_openai_client):
    """
    Tests that the workflow raises FileNotFoundError if the file doesn't exist.
    """
    with pytest.raises(FileNotFoundError, match="File not found"):
        run_abnt_workflow(mock_openai_client, {"file_path": "/invalid/path.docx"})


@patch('src.academic_agent.workflows.abnt_workflow._read_text_from_file', side_effect=ValueError("Unsupported format"))
def test_run_abnt_workflow_unsupported_format(mock_read_file, mock_openai_client):
    """
    Tests that the workflow raises ValueError for unsupported file formats.
    """
    with pytest.raises(ValueError, match="Unsupported format"):
        run_abnt_workflow(mock_openai_client, {"file_path": "/fake/path/document.txt"})


@patch('src.academic_agent.workflows.abnt_workflow._read_text_from_file', return_value="Texto para formatar.")
def test_run_abnt_workflow_api_failure(mock_read_file, mock_openai_client):
    """
    Tests that the workflow raises a ValueError if the API response is invalid.
    """
    params = {"file_path": "/fake/path/document.pdf"}

    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = None
    mock_openai_client.chat.completions.create.return_value = mock_response

    with pytest.raises(ValueError, match="Failed to get a valid response from the API."):
        run_abnt_workflow(mock_openai_client, params) 