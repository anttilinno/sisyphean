import json
from types import NoneType

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.core.config import settings
from app.tests.utils.todo import create_random_todo


def test_create_item(client: TestClient) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/todos",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()

    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content


def test_fetch_todo(client: TestClient, db: Session) -> None:
    todo = create_random_todo(db, 1)[0]
    # When
    response = client.get(f"{settings.API_V1_STR}/todos/{todo.id}")
    # Then
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == todo.title
    assert data["description"] == todo.description
    assert data["id"] == todo.id


def test_fetch_todos(client: TestClient, db: Session) -> None:
    todo1, todo2 = create_random_todo(db, 2)
    # When
    response = client.get(f"{settings.API_V1_STR}/todos")

    # Then
    assert response.status_code == 200
    data = response.json()
    ids_in_database = list(map(lambda item: item["id"], data))
    todo1_from_response = list(filter(lambda item: item["id"] == todo1.id, data))
    assert todo1.id in ids_in_database
    assert todo2.id in ids_in_database
    assert len(todo1_from_response) == 1
    assert todo1_from_response[0]["title"] == todo1.title
    assert todo1_from_response[0]["description"] == todo1.description


def test_update_todo(client: TestClient, db: Session) -> None:
    todo = create_random_todo(db, 1)[0]

    data = {"title": "Bingo", "description": "Bongo"}
    response = client.put(
        f"{settings.API_V1_STR}/todos/{todo.id}",
        json=data,
    )
    # Then
    assert response.status_code == 200
    content = response.json()

    assert content["title"] == "Bingo"
    assert content["description"] == "Bongo"
    assert "id" in content


def test_delete_todo(client: TestClient, db: Session) -> None:
    todo = create_random_todo(db, 1)[0]
    # When
    response = client.delete(f"{settings.API_V1_STR}/todos/{todo.id}")

    # Then
    assert response.status_code == 200

    data = response.json()

    assert todo.id == data["id"]

    statement = text("SELECT id FROM todo WHERE id = :id")
    r = db.execute(statement, {"id": data["id"]})

    assert type(r.first()) == NoneType
