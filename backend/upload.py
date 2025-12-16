
from fastapi import APIRouter, UploadFile, File
from database import documents_db

router = APIRouter()

@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")
    documents_db["default"] = content
    return {"message": "Document uploaded successfully"}
