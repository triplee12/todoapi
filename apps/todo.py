#!/usr/bin/python3
"""Todo module."""
from typing import List
from fastapi import APIRouter
from schemas.todos import TodosSchema, TodosRes

todo_router: APIRouter = APIRouter(prefix="/todos", tags=["Todos"])
todos_list: list[dict[str, str]] = [
    {"id": 1, "title": "Todos 1", "desc": "Todos description 1"},
    {"id": 2, "title": "Todo 2", "desc": "Todos description 2"}
]


@todo_router.get("/", response_model=List[TodosRes])
async def get_todos() -> list[dict[int, str, str]]:
    """Get list of all available Todos."""
    return todos_list


@todo_router.post("/create")
async def add_todos(todo: TodosSchema) -> dict:
    """Add a new Todos to the list of avaikable Todos.

    Returns:
        dict: todos object
    """
    todos_list.append(todo)
    return {"message": "New Todos added successfully"}
