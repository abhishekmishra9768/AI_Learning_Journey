"""Day 06 - Document loading and keyword search.

Purpose: load_documents() reads the .txt files in knowledge/, and
retrieve() is a simple keyword search that does not use embeddings.
"""

from pathlib import Path

def load_documents():
    """Read every .txt file in the knowledge/ folder.

    Returns a dictionary: {file name: file text}.
    """

    documents = {}

    folder = Path("knowledge")

    for file in folder.glob("*.txt"):

        documents[file.name]= file.read_text(encoding="utf-8")

    return documents


def retrieve(question):
    """Simple keyword search (no embeddings).

    Returns (file name, text) of the first document that contains the
    question text, or (None, None) if there is no match.
    """

    documents = load_documents()

    question = question.lower()

    for filename, content in documents.items():

        if question in content.lower():

            return filename, content

    return None, None
