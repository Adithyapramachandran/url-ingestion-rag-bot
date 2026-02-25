from fastapi import APIRouter
from app.services.rag_pipeline import answer_question

router = APIRouter()

@router.post("/")   # ✅ NOT /chat
def chat(data: dict):
    question = data["question"]
    answer = answer_question(question)
    return {"answer": answer}
