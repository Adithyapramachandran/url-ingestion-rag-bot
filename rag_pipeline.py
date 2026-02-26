from transformers import pipeline
from app.db.vector_store import db

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def answer_question(question: str):

    docs = db.similarity_search(question, k=3)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    Answer based on context:

    {context}

    Question: {question}
    """

    result = generator(prompt, max_length=256)

    return result[0]["generated_text"]