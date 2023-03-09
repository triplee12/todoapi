#!/usr/bin/python3
"""Todo module."""
from fastapi import APIRouter

todo_router: APIRouter = APIRouter(prefix="/todos", tags=["Todos"])
todos_list: list[dict[str, str]] = [
    {"id": 1, "title": "Todos 1", "description": "Todos description 1"},
    {"id": 2, "title": "Todo 2", "description": "Todos description 2"}
]


@todo_router.get("/")
async def get_todos() -> dict[str, list[dict[str, str]]]:
    """Get list of all available Todos."""
    return {
        "todos": todos_list
    }


@todo_router.post("/create")
async def add_todos(todo: dict) -> dict:
    """Add a new Todos to the list of avaikable Todos.

    Returns:
        dict: todos object
    """
    todos_list.append(todo)
    return {"message": "New Todos added successfully"}
