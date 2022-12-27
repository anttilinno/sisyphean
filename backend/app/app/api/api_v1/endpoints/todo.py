from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/{todo_id}", status_code=200)
def fetch_todo(todo_id) -> Any:
    """
    Fetch a single todo by ID
    """

    return {"todo": todo_id}


@router.get("/", status_code=200)
def fetch_todos() -> Any:
    """
    Fetch all todos
    """

    return [{"todo": 1}, {"todo": 2}]
