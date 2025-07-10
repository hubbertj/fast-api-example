from fastapi import FastAPI
from controllers.book_controller import router as book_router
from controllers.home_controller import router as home_router

app = FastAPI()

# Include routers for modular route management
app.include_router(book_router)
app.include_router(home_router)