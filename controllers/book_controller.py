from fastapi import APIRouter
from services import book_service

router = APIRouter()

@router.get("/books")
async def get_books():
    return book_service.get_books()

@router.get("/books/{book_id}")
async def get_book(book_id: int):
    return book_service.get_book(book_id)

@router.post("/books")
async def create_book(book: dict):
    return book_service.create_book(book)

@router.put("/books/{book_id}")
async def update_book(book_id: int, book: dict):
    return book_service.update_book(book_id, book)

@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    return book_service.delete_book(book_id)


