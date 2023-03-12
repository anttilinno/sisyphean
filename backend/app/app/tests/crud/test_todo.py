from sqlalchemy.orm import Session

from app import crud
from app.schemas.todo import TodoCreate, TodoUpdate
from app.tests.utils.utils import random_lower_string


def test_create_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    todo = crud.todo.create(db=db, obj_in=todo_in)
    assert todo.title == title
    assert todo.description == description


def test_get_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    todo = crud.todo.create(db=db, obj_in=todo_in)
    stored_todo = crud.todo.get(db=db, id=todo.id)
    assert stored_todo
    assert todo.id == stored_todo.id
    assert todo.title == stored_todo.title
    assert todo.description == stored_todo.description


def test_update_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    todo = crud.todo.create(db=db, obj_in=todo_in)
    description2 = random_lower_string()
    todo_update = TodoUpdate(description=description2)
    todo2 = crud.todo.update(db=db, db_obj=todo, obj_in=todo_update)
    assert todo.id == todo2.id
    assert todo.title == todo2.title
    assert todo2.description == description2


def test_delete_todo(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    todo_in = TodoCreate(title=title, description=description)
    todo = crud.todo.create(db=db, obj_in=todo_in)
    todo2 = crud.todo.remove(db=db, id=todo.id)
    todo3 = crud.todo.get(db=db, id=todo.id)
    assert todo3 is None
    assert todo2.id == todo.id
    assert todo2.title == title
    assert todo2.description == description
