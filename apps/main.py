#!/bin/python3
"""ToDo main module."""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .todo import todo_router

templates: Jinja2Templates = Jinja2Templates(directory="templates")
app: FastAPI = FastAPI()


@app.get("/")
async def root(request: Request) -> dict[str, str]:
    """Root route for ToDOAPI."""
    return templates.TemplateResponse("base.html", {"request": request})


app.include_router(todo_router)
