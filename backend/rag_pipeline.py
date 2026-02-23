# Implement RAG retrieval and answer generation pipeline
import os
from app.db.vector_store import get_db
from openai import OpenAI

client = OpenAI()

def answer_question(question):
    db = get_db()

    docs = db.similarity_search(question, k=3)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Answer using context.

Context:
{context}

Question:
{question}
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content
