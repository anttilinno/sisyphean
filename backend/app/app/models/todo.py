from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Todo(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
