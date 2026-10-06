"""Day 06 - Manual test for retriever.py.

How to run (from inside the Day06 folder):
    python test_retriever.py
It prints all documents and tests the keyword search.
"""

from retriever import load_documents
import json

from retriever import retrieve

# Load all documents and print them as formatted JSON
documents = load_documents()
print(json.dumps(documents,indent=2))
print("\n")

# Print each document with a separator line
for name, text in documents.items():

    print(name)

    print(text)

    print("-" * 40)


# Test the keyword search
filename, content = retrieve("Abhishek")

print(filename)

print()

print(content)
