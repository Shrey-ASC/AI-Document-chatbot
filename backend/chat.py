from fastapi import APIRouter, HTTPException
from llm import ask_llm, summarize_document
from database import documents_db, chats_db

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    question = data.get("question")
    context = documents_db.get("default", "")

    if not context:
        raise HTTPException(status_code=400, detail="No document uploaded")

    answer = ask_llm(context, question)
    chats_db.append({"q": question, "a": answer})

    return {"answer": answer}


@router.post("/summarize-document")
def summarize():
    context = documents_db.get("default", "")

    if not context:
        raise HTTPException(status_code=400, detail="No document uploaded")

    summary = summarize_document(context)
    return {"summary": summary}
