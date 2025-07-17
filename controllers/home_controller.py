from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/")
async def health_check():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"health": "good", "dateTime": time + " UTC", "message": "Welcome to the Book API!"}



