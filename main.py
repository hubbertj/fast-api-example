from fastapi import FastAPI
from controllers.book_controller import router as book_router
from controllers.home_controller import router as home_router

booksApp = FastAPI()

# Include routers for modular route management
booksApp.include_router(book_router)
booksApp.include_router(home_router)