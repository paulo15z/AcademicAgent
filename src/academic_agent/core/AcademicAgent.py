import openai
from typing import Any, Dict, Optional
from src.academic_agent.workflows.writing_workflow import run_writing_workflow
from src.academic_agent.workflows.abnt_workflow import run_abnt_workflow
from src.academic_agent.workflows.summarization_workflow import run_summarization_workflow

class AcademicAgent:
    """
    O Agente Acadêmico principal para orquestrar workflows e interagir com modelos de LLM.

    Esta classe é o núcleo do sistema, responsável por gerenciar a execução de tarefas
    acadêmicas, interagir com a API da OpenAI e garantir que os dados sejam validados
    e estruturados corretamente.
    """

    def __init__(self, openai_api_key: Optional[str] = None):
        """
        Inicializa o AcademicAgent.

        Args:
            openai_api_key (Optional[str]): A chave da API da OpenAI. Se não for fornecida,
                                             o sistema tentará usar a variável de ambiente
                                             OPENAI_API_KEY.
        """
        if openai_api_key:
            openai.api_key = openai_api_key
        
        self.client = openai.OpenAI()

    def run_task(self, task_name: str, params: Dict[str, Any]) -> Any:
        """
        Executa uma tarefa acadêmica específica.

        Este método atuará como um dispatcher, chamando o workflow apropriado
        com base no nome da tarefa fornecida.

        Args:
            task_name (str): O nome da tarefa a ser executada (ex: 'writing', 'revisao').
            params (Dict[str, Any]): Um dicionário de parâmetros para a tarefa.

        Returns:
            Any: O resultado da execução da tarefa.
        
        Raises:
            ValueError: Se o nome da tarefa for desconhecido.
        """
        # Mapeamento de tarefas para funções de workflow
        workflows = {
            "writing": run_writing_workflow,
            "abnt_formatting": run_abnt_workflow,
            "summarization": run_summarization_workflow
        }

        workflow_func = workflows.get(task_name)
        
        if workflow_func:
            return workflow_func(self.client, params)
        else:
            raise ValueError(f"Tarefa desconhecida: {task_name}")

    def __repr__(self) -> str:
        """
        Representação oficial do objeto.
        """
        return "AcademicAgent()"

    def __str__(self) -> str:
        """
        Representação em string do objeto.
        """
        return "Agente Acadêmico de IA"
