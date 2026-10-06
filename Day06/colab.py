from retriever import load_documents
from embeddings_rag import create_embedding
from similart import cosine_similarity

documents = load_documents()
doc_embeddings = {name: create_embedding(text) for name, text in documents.items()}

question = "what is machine learning"
q_emb = create_embedding(question)

for name, emb in doc_embeddings.items():
    print(name, cosine_similarity(q_emb, emb))
