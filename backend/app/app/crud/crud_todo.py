from .base import CRUDBase
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

todo = CRUDBase[Todo, TodoCreate, TodoUpdate](Todo)
