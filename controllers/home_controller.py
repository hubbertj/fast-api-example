from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_books():
    return {"message": "Home page"}

@router.post("/")
@router.put("/")
@router.delete("/")
async def create_update_delete_book(book: dict):
    return {"message": "Create, update, or delete book", "book": book}


