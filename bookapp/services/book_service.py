from datetime import datetime
from bookapp.schemas.book_schema import BookSchema as bookModel

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

def create_book(book: bookModel):
    """
    Creates a new book and adds it to the list.
    """
    new_book = book.dict()
    new_book['id'] = len(Books) + 1  # Assign a new ID
    Books.append(new_book)
    return new_book

def update_book_by_author(book: bookModel):
    """
    Updates an existing book by its author.
    """
    for i, existing_book in enumerate(Books):
        if existing_book['author'].lower() == book.author.lower():
            Books[i] = book.dict()
            return Books[i]
    return None

def delete_book(book_title: str):
    """
    Deletes a book by its title.
    """
    for i, book in enumerate(Books):
        if book['title'].lower() == book_title.lower():
            del Books[i]
            return True
    return False

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





