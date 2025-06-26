import pytest
from unittest.mock import MagicMock
from openai import OpenAI
from src.academic_agent.workflows.writing_workflow import run_writing_workflow

@pytest.fixture
def mock_openai_client():
    """Cria um cliente OpenAI simulado para os testes."""
    return MagicMock(spec=OpenAI)

def test_run_writing_workflow_success(mock_openai_client):
    """
    Testa o caminho de sucesso do workflow de redação.
    """
    # Prepara a resposta simulada da API
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message = MagicMock()
    mock_response.choices[0].message.content = "Texto gerado com sucesso."
    mock_openai_client.chat.completions.create.return_value = mock_response

    params = {"prompt": "Um prompt de teste"}
    result = run_writing_workflow(mock_openai_client, params)

    assert result == "Texto gerado com sucesso."
    mock_openai_client.chat.completions.create.assert_called_once()

def test_run_writing_workflow_no_prompt(mock_openai_client):
    """
    Testa se um ValueError é levantado quando nenhum prompt é fornecido.
    """
    params = {}
    with pytest.raises(ValueError, match="O parâmetro 'prompt' é obrigatório para o workflow de redação."):
        run_writing_workflow(mock_openai_client, params)

def test_run_writing_workflow_api_error(mock_openai_client):
    """
    Testa o tratamento de erro quando a API da OpenAI falha.
    """
    mock_openai_client.chat.completions.create.side_effect = Exception("Falha na API")

    params = {"prompt": "Um prompt que causará erro"}
    result = run_writing_workflow(mock_openai_client, params)

    assert result == "Não foi possível gerar o texto devido a um erro no workflow." 