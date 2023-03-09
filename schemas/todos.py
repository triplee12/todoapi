#!/usr/bin/python3
"""Todos schema for data validation."""
from pydantic import BaseModel


class TodosSchema(BaseModel):
    """Todos schema for todo post validation."""

    id: int
    title: str
    desc: str

    class Config:
        """Configuration for documentation."""

        Schema_extra: dict[str, dict[str, str]] = {
            "Example": {
                "id": 1,
                "title": "Title here",
                "desc": "Description here"
            }
        }
        orm_mode: bool = True


class TodoItem(BaseModel):
    """Todo schema for retrieving single todo."""

    title: str
    desc: str

    class Config:
        """Configuration for documentation."""

        Schema_extra: dict[str, dict[str, str]] = {
            "Example": {
                "title": "Title here",
                "desc": "Description here"
            }
        }
