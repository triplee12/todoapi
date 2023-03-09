#!/bin/python3
"""ToDo main module."""
from fastapi import FastAPI
from .todo import todo_router

app: FastAPI = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """Root route for ToDOAPI."""
    return {"message": "Welcome to FastAPI ToDoAPI"}


app.include_router(todo_router)
