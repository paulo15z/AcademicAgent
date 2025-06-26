"""
Workflow for formatting text from a DOCX or PDF file according to ABNT standards.
"""

from openai import OpenAI

from ..validation import schemas
from ..utils.file_parser import read_text_from_file


def run_abnt_workflow(client: OpenAI, params: schemas.ABNTWorkflowParams) -> str:
    """
    Runs the ABNT formatting workflow on a file.

    This function takes a file path, extracts the text, and uses an OpenAI model
    to format it according to ABNT (Brazilian Association of Technical Standards) rules.

    Args:
        client (OpenAI): The OpenAI client instance.
        params (schemas.ABNTWorkflowParams): The parameters for the workflow,
                                             validated by Pydantic.

    Returns:
        str: The text formatted according to ABNT standards.

    Raises:
        ValueError: If the file is invalid or the API call fails.
    """
    text_to_format = read_text_from_file(params.file_path)

    if not text_to_format.strip():
        return "The file is empty or contains no readable text."

    system_prompt = (
        "Você é um especialista em formatação de textos acadêmicos segundo as normas da ABNT. "
        "Sua tarefa é reformatar o texto fornecido para que ele siga estritamente as regras da ABNT, "
        "incluindo citações, referências, formatação de parágrafos, e estrutura geral. "
        "Não altere o conteúdo semântico, apenas a formatação."
    )

    response = client.chat.completions.create(
        model=params.model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_to_format},
        ],
        temperature=0.3,
    )

    formatted_text = response.choices[0].message.content
    if formatted_text is None:
        raise ValueError("Failed to get a valid response from the API.")

    return formatted_text 