from fastapi import FastAPI
from controllers.book_controller import router as book_router

app = FastAPI()
app.include_router(book_router)