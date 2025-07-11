from datetime import date
from typing import Optional
from fastapi import APIRouter
from services import book_service
from schemas.book_schema import BookSchema as bookModel

router = APIRouter()

@router.get("/books")
async def get_books():
    return book_service.get_books()

@router.get("/books/author/{author}/")
async def get_books_by_author(author: str, from_date: Optional[date] = None):
    if from_date:
        return book_service.get_books_by_author_and_date(author, from_date)
    return book_service.search_books(author)

@router.get("/books/title/{title}")
async def get_books_by_title(title: str):
    return book_service.get_books_by_title(title)

@router.get("/books/{book_id}")
async def get_book(book_id: int):
    return book_service.get_book(book_id)

@router.post("/books")
async def create_book(book: bookModel):
    return book_service.create_book(book)

@router.put("/books")
async def update_book(book: bookModel):
    return book_service.update_book_by_author(book)

@router.delete("/books/{title}")
async def delete_book(book_title: str):
    return book_service.delete_book(book_title)


