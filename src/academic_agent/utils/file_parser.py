"""
Utilities for parsing text from different file formats.
"""

import os
import fitz  # PyMuPDF
import docx

def read_text_from_file(file_path: str) -> str:
    """
    Reads text content from a .docx or .pdf file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The extracted text from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is not supported.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")

    _, extension = os.path.splitext(file_path)
    text = ""

    if extension.lower() == ".pdf":
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()  # type: ignore
    elif extension.lower() == ".docx":
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        raise ValueError(f"Unsupported file format: {extension}. Please use .pdf or .docx.")

    return text 