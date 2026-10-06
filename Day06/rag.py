"""Day 06 - RAG (Retrieval Augmented Generation) assistant.

Purpose: answers questions using your own documents.
    1. Load all .txt files from the knowledge/ folder.
    2. Create an embedding for each document (embeddings_rag.py).
    3. Embed the user's question and find the most similar document
       (similart.py).
    4. Send that document to Claude as context and print the answer.

How to run (from inside the Day06 folder, so knowledge/ is found):
    pip install sentence-transformers anthropic
    python rag.py
Requires ANTHROPIC_API_KEY. Type "quit" to exit.
"""

import anthropic
from retriever import *
from embeddings_rag import *
from similart import *

# Create the API client (reads ANTHROPIC_API_KEY from the environment)
client = anthropic.Anthropic()

print("*" * 40)
print("My AI Assistant")
print("*" * 40)

# Step 1: load every .txt file from the knowledge/ folder
documents = load_documents()

# Step 2: create an embedding for each document and keep it by file name
document_embeddings = {}

for filename, content in documents.items():

    document_embeddings[filename] = create_embedding(content)


while True:
    user_input = input("\nYou : ")

    # Exit the program when the user types "quit"
    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    # Step 3: turn the question into an embedding too
    question_embedding = create_embedding(user_input)

    best_score = -1

    best_document = None

    # Step 4: find the document whose embedding is most similar to the question
    for filename, embedding in document_embeddings.items():

        score = cosine_similarity(question_embedding, embedding)

        if score > best_score:

            best_score = score

            best_document = filename

    # Step 5: use the best-matching document as context for Claude
    context = documents[best_document]

    prompt = f"""
Answer the question using only
the following information.

Context:

{context}

Question:

{user_input}
"""

    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )

    # Print only the text blocks of the answer
    for block in response.content:
        if block.type == "text":
            print("\nAI  :", block.text)
