
from fastapi import APIRouter
from llm import ask_llm
from database import documents_db, chats_db

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    question = data["question"]
    context = documents_db.get("default", "")
    answer = ask_llm(context, question)
    chats_db.append({"q": question, "a": answer})
    return {"answer": answer}
