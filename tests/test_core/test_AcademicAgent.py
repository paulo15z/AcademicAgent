import pytest
from src.academic_agent.core.AcademicAgent import AcademicAgent
from unittest.mock import MagicMock

def test_academic_agent_initialization():
    """
    Testa se o AcademicAgent é inicializado corretamente.
    """
    agent = AcademicAgent()
    assert agent is not None
    assert str(agent) == "Agente Acadêmico de IA"
    assert repr(agent) == "AcademicAgent()"

def test_run_task_with_valid_task(mocker):
    """
    Testa a execução de uma tarefa válida através do run_task, que deve despachar para o workflow correto.
    """
    # Simula o workflow de redação para que não seja realmente executado
    mock_writing_workflow = mocker.patch(
        'src.academic_agent.core.AcademicAgent.run_writing_workflow',
        return_value="Resultado do workflow de redação."
    )

    agent = AcademicAgent()
    prompt_text = "Explique a teoria da relatividade."
    params = {"prompt": prompt_text}
    
    result = agent.run_task("writing", params)
    
    # Verifica se o resultado é o esperado
    assert result == "Resultado do workflow de redação."
    
    # Verifica se a função do workflow foi chamada com os parâmetros corretos
    mock_writing_workflow.assert_called_once_with(agent.client, params)

def test_run_task_for_abnt_formatting(mocker):
    """
    Testa o despacho para o workflow de formatação ABNT.
    """
    # Mock do workflow de ABNT
    mock_abnt_workflow = mocker.patch(
        'src.academic_agent.core.AcademicAgent.run_abnt_workflow',
        return_value="Texto formatado em ABNT."
    )

    agent = AcademicAgent()
    params = {"file_path": "/fake/path/document.docx"}
    
    result = agent.run_task("abnt_formatting", params)
    
    # Verifica se o resultado é o esperado
    assert result == "Texto formatado em ABNT."
    
    # Verifica se a função do workflow foi chamada corretamente
    mock_abnt_workflow.assert_called_once_with(agent.client, params)

def test_run_task_with_invalid_task():
    """
    Testa se run_task levanta um ValueError para uma tarefa desconhecida.
    """
    agent = AcademicAgent()
    with pytest.raises(ValueError, match="Tarefa desconhecida: non_existent_task"):
        agent.run_task("non_existent_task", {})