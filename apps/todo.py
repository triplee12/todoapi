#!/usr/bin/python3
"""Todo module."""
from typing import List
from fastapi import APIRouter, Path, HTTPException, status
from schemas.todos import TodosSchema, TodoItem

todo_router: APIRouter = APIRouter(prefix="/todos", tags=["Todos"])
todos_list: list[dict[int, str, str]] = [
    {"id": 1, "title": "Todos 1", "desc": "Todos description 1"},
    {"id": 2, "title": "Todo 2", "desc": "Todos description 2"}
]


def retrieve(todo_id: int) -> dict:
    """Return single todo."""
    for todo in todos_list:
        if todo["id"] == todo_id:
            return todo


def idx(todo_id: int) -> int:
    """Index of todo in todos_list."""
    for i in range(len(todos_list)):
        if todos_list[i]["id"] == todo_id:
            return i


@todo_router.get("/", response_model=List[TodosSchema])
async def get_todos() -> list[dict[int, str, str]]:
    """Get list of all available Todos."""
    return todos_list


@todo_router.post("/create", status_code=status.HTTP_201_CREATED)
async def add_todos(todo: TodosSchema) -> dict:
    """Add a new Todos to the list of avaikable Todos.

    Returns:
        dict: todos object
    """
    todos_list.append(todo.dict())
    print(todos_list)
    return {"message": "New Todos added successfully"}


@todo_router.get("/{todo_id}", response_model=TodoItem)
async def get_single_todo(todo_id: int = Path(..., ge=1, le=100)) -> dict:
    """Retrive todo."""
    todo: dict = retrieve(todo_id)
    if todo:
        return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo not found"
    )


@todo_router.put(
        "/update/{todo_id}",
        status_code=status.HTTP_201_CREATED,
        response_model=TodoItem
    )
async def update_todo(
    to_update: TodoItem,
    todo_id: int = Path(..., ge=1, le=100)
) -> dict:
    """Update todo item."""
    todo: dict = retrieve(todo_id)
    if todo:
        todo["title"] = to_update.title
        todo["desc"] = to_update.desc
        return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo not found"
    )


@todo_router.delete("/delete/{todo_id}")
async def del_todo(todo_id: int) -> dict[str, str]:
    """Delete todo item."""
    todo: dict = retrieve(todo_id)
    if todo:
        index: int = idx(todo_id)
        todos_list.pop(index)
        return {"delete": "successful"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo not found"
    )


@todo_router.delete("/all/delete")
async def del_all_todos() -> dict[str, str]:
    """Delete all todos."""
    todos_list.clear()
    return {"message": "You don't have active todos."}
