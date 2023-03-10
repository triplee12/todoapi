#!/usr/bin/python3
"""Todos schema for data validation."""
from typing import Optional
from fastapi import Form
from pydantic import BaseModel


class TodosSchema(BaseModel):
    """Todos schema for todo post validation."""

    id: Optional[int]
    title: str
    desc: str

    @classmethod
    def as_form(cls, title: str = Form(...), desc: str = Form(...)):
        """Serve as a form."""
        return cls(title=title, desc=desc)

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
