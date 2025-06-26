from typing import Dict, Any
from openai import OpenAI

def run_writing_workflow(client: OpenAI, params: Dict[str, Any]) -> str:
    """
    Executa o workflow de redação acadêmica.

    Este workflow recebe um prompt e utiliza o modelo de linguagem para gerar
    um texto com base nele. É o ponto de partida para tarefas de escrita mais
    complexas.

    Args:
        client (OpenAI): O cliente da API da OpenAI a ser utilizado.
        params (Dict[str, Any]): Um dicionário contendo os parâmetros para o workflow.
                                 Deve incluir a chave 'prompt'.

    Returns:
        str: O texto gerado pelo modelo.
    
    Raises:
        ValueError: Se o parâmetro 'prompt' não for fornecido.
    """
    prompt = params.get("prompt")
    if not prompt:
        raise ValueError("O parâmetro 'prompt' é obrigatório para o workflow de redação.")

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "Você é um assistente de redação acadêmica."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000  # Aumentando para permitir textos mais longos
        )
        
        content = response.choices[0].message.content
        return content.strip() if content else ""
    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API da OpenAI no workflow de redação: {e}")
        return "Não foi possível gerar o texto devido a um erro no workflow." 