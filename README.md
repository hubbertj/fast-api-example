# FastAPI Project

This is a Python project that uses [FastAPI](https://fastapi.tiangolo.com/) for building APIs. A virtual environment named `fastapienv` is used for dependency management.

## 🚀 Features

- FastAPI backend
- Virtual environment setup with `venv`
- Easy installation and run instructions

## 📁 Project Structure


## 📦 Dependencies
- `fastapi`: The main framework for building APIs.
- `uvicorn`: ASGI server for running FastAPI applications.
- `pydantic`: Data validation and settings management using Python type annotations.
- `requests`: For making HTTP requests.
- `python-dotenv`: For loading environment variables from a `.env` file.
- `pytest`: For testing the application.
- `httpx`: For making asynchronous HTTP requests.
- `sqlalchemy`: SQL toolkit and Object-Relational Mapping (ORM) system.


## Create a Virtual Environment (if not already created)
  ```bash
    python3 -m venv fastapienv
  ```
### Activate the Virtual Environment
  ```bash
    source fastapienv/bin/activate
  ```
### Deactivate the Environment
  ```bash
    deactivate
  ```
### Install Dependencies
  ```bash
    pip install -r requirements.txt
  ``` 
### Run the Application
  ```bash
    uvicorn main:app --reload
  ```
### view all packages installed in the virtual environment
  ```bash 
    pip list
  ``` 


