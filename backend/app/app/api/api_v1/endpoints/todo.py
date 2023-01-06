from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Todo])
def read_todos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve todos.
    """

    return crud.todo.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Todo)
def create_todo(
    *,
    db: Session = Depends(deps.get_db),
    todo_in: schemas.TodoCreate,
) -> Any:
    """
    Create new todo.
    """
    return crud.todo.create(db=db, obj_in=todo_in)


@router.put("/{id}", response_model=schemas.Todo)
def update_todo(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    todo_in: schemas.TodoUpdate,
) -> Any:
    """
    Update an todo.
    """
    todo = crud.todo.get(db=db, id=id)

    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")

    return crud.todo.update(db=db, db_obj=todo, obj_in=todo_in)


@router.get("/{id}", response_model=schemas.Todo)
def read_todo(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get todo by ID.
    """
    todo = crud.todo.get(db=db, id=id)

    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")

    return todo


@router.delete("/{id}", response_model=schemas.Todo)
def delete_todo(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an todo.
    """
    todo = crud.todo.get(db=db, id=id)

    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")

    todo = crud.todo.remove(db=db, id=id)

    return todo
