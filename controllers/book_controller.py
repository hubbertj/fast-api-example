from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
async def get_books():
    return {"message": "List of books"}

@router.get("/books/{book_id}")
async def get_book(book_id: int):
    return {"message": f"Details of book {book_id}"}

@router.post("/books")
async def create_book(book: dict):
    return {"message": "Book created", "book": book}

@router.put("/books/{book_id}")
async def update_book(book_id: int, book: dict):
    return {"message": f"Book {book_id} updated", "book": book}

@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    return {"message": f"Book {book_id} deleted"}


