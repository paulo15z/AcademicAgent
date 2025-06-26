"""
Integration tests for the AcademicAgent and its workflows.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.academic_agent.core.AcademicAgent import AcademicAgent

@pytest.fixture
def agent():
    """Fixture to create an AcademicAgent with a mocked OpenAI client."""
    with patch('src.academic_agent.core.AcademicAgent.openai.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        # Pass the mocked client to the agent's client attribute directly after initialization
        agent_instance = AcademicAgent()
        agent_instance.client = mock_client
        yield agent_instance

def test_agent_run_writing_workflow_integration(agent):
    """
    Tests the integration of the AcademicAgent with the writing workflow.
    """
    # Arrange
    params = {"prompt": "Escreva sobre IA."}
    expected_result = "Texto sobre IA gerado com sucesso."
    
    # Mock the response from the LLM for the writing workflow
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = expected_result
    agent.client.chat.completions.create.return_value = mock_response

    # Act
    result = agent.run_task("writing", params)

    # Assert
    assert result == expected_result
    agent.client.chat.completions.create.assert_called_once()
    _, call_kwargs = agent.client.chat.completions.create.call_args
    assert params["prompt"] in call_kwargs["messages"][1]["content"]


@patch('src.academic_agent.workflows.abnt_workflow._read_text_from_file', return_value="Texto do arquivo.")
def test_agent_run_abnt_workflow_integration(mock_read_file, agent):
    """
    Tests the integration of the AcademicAgent with the ABNT workflow.
    """
    # Arrange
    params = {"file_path": "/fake/path/documento.pdf"}
    expected_result = "Texto formatado em ABNT."
    
    # Mock the response from the LLM for the ABNT workflow
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = expected_result
    agent.client.chat.completions.create.return_value = mock_response

    # Act
    result = agent.run_task("abnt_formatting", params)

    # Assert
    assert result == expected_result
    mock_read_file.assert_called_once_with(params["file_path"])
    agent.client.chat.completions.create.assert_called_once()
    _, call_kwargs = agent.client.chat.completions.create.call_args
    assert "Texto do arquivo." in call_kwargs["messages"][1]["content"]
    assert "ABNT" in call_kwargs["messages"][0]["content"]

def test_agent_run_summarization_workflow_integration(agent):
    """
    Tests the integration of the AcademicAgent with the summarization workflow.
    """
    # Arrange
    params = {"text": "Este é um texto para resumir."}
    expected_result = "Este é o resumo."
    
    # Mock the response from the LLM
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = expected_result
    agent.client.chat.completions.create.return_value = mock_response

    # Act
    result = agent.run_task("summarization", params)

    # Assert
    assert result == expected_result
    agent.client.chat.completions.create.assert_called_once()
    _, call_kwargs = agent.client.chat.completions.create.call_args
    assert params["text"] in call_kwargs["messages"][1]["content"]
    assert "sintetizar informações" in call_kwargs["messages"][0]["content"]

def test_agent_run_nonexistent_workflow(agent):
    """
    Tests that the agent raises a ValueError for a non-existent workflow.
    """
    with pytest.raises(ValueError, match="Tarefa desconhecida: nonexistent"):
        agent.run_task("nonexistent", {}) 