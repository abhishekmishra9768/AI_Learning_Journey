"""Day 06 - Embedding helper.

Purpose: loads a local embedding model and exposes create_embedding(),
which turns text into a vector of numbers. No API key is needed for this
file; the model runs on your own machine.

Requires: pip install sentence-transformers
"""

from sentence_transformers import SentenceTransformer

# Load the local embedding model (downloaded from HuggingFace on first use)
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5")


# Creates an embedding (a list of numbers) for a piece of text,
# used for every document and every user question

def create_embedding(content):
    # encode() returns a vector; similar texts give similar vectors
    return model.encode(content)


# Example: compare two sentences by meaning
# text1 = "Python is a programming language."

# text2 = "Python is used for software development."

# embedding1 = model.encode(text1)

# embedding2 = model.encode(text2)


# Length of each vector
# print(len(embedding1))
# print(len(embedding2))

# Similarity score: closer to 1 means more similar
# score = cosine_similarity(embedding1, embedding2)

# print(score)
