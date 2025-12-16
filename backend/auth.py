
from fastapi import APIRouter, HTTPException
from database import users_db

router = APIRouter()

@router.post("/register")
def register(data: dict):
    if data["email"] in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[data["email"]] = data["password"]
    return {"message": "Registered successfully"}

@router.post("/login")
def login(data: dict):
    if users_db.get(data["email"]) != data["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
