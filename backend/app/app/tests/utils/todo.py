from typing import List
from faker import Faker
from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.todo import TodoCreate


def create_random_todo(db: Session, todoCount: int) -> List[models.Todo]:
    fake = Faker()
    return [
        crud.todo.create(
            db=db, obj_in=TodoCreate(title=fake.name(), description=fake.address())
        )
        for i in range(todoCount)
    ]
