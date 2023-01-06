from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class TodoCreate(TodoBase):
    title: str


class TodoUpdate(TodoBase):
    pass


class TodoInDBBase(TodoBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class Todo(TodoInDBBase):
    pass


class TodoInDB(TodoInDBBase):
    pass
