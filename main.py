from fastapi import FastAPI
from bookapp.controllers.book_controller import router as book_app_book_router
from bookapp.controllers.home_controller import router as book_app_home_router
from todoapp.controllers.home_controller import router as todo_app_home_router

booksApp = FastAPI()
todoApp = FastAPI()

# Include routers for modular route management
booksApp.include_router(book_app_book_router)
booksApp.include_router(book_app_home_router)

todoApp.include_router(todo_app_home_router)