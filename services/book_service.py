from datetime import datetime
from schemas.book_schema import BookSchema as book_model

Books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'id': 2,'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'id': 3,'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'id': 4,'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813},
    {'id': 5,'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951},
    {'id': 6,'title': 'Brave New World', 'author': 'Aldous Huxley', 'year': 1932},
    {'id': 7,'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'year': 1953},
    {'id': 8,'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937},
    {'id': 9,'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'year': 1954},
    {'id': 10,'title': 'Animal Farm', 'author': 'George Orwell', 'year': 1945}
]

def get_books():
    """
    Returns a list of books.
    """
    return Books

def get_books_by_title(title: str):
    """
    Returns a list of books that match the given title.
    """
    results = []
    for book in Books:
        if title.lower() in book['title'].lower():
            results.append(book)
    return results

def get_book(book_id: int):
    """
    Returns a book by its ID.
    """
    if 0 <= book_id < len(Books):
        return Books[book_id]
    else:
        return None

def create_book(book: book_model):
    """
    Creates a new book and adds it to the list.
    """
    new_book = book.dict()
    new_book['id'] = len(Books) + 1  # Assign a new ID
    Books.append(new_book)
    return new_book

def update_book(book_id: int, book: dict):
    """
    Updates an existing book by its ID.
    """
    if 0 <= book_id < len(Books):
        Books[book_id] = book
        return book
    else:
        return None

def delete_book(book_id: int):
    """
    Deletes a book by its ID.
    """
    if 0 <= book_id < len(Books):
        return Books.pop(book_id)
    else:
        return None

def search_books(query: str):
    """
    Searches for books by title or author.
    """
    results = []
    for book in Books:
        if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
            results.append(book)
    return results

def get_books_by_author_and_date(author: str, date: datetime.date):
    """
    Returns a list of books by a specific author and published on or before the given date.
    """
    results = []
    for book in Books:
        if book['author'].lower() == author.lower() and book['year'] <= date.year:
            results.append(book)
    return results





