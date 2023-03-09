#!/usr/bin/python3
"""Todos schema for data validation."""
from pydantic import BaseModel


class TodosSchema(BaseModel):
    """Todos schema for todo post validation."""

    id: int
    title: str
    desc: str


class TodosRes(TodosSchema):
    """Todos schema for todo get validation."""
