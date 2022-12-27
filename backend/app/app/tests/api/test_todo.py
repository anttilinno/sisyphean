from app.core.config import settings


def test_fetch_todos(client):
    # When
    response = client.get(f"{settings.API_V1_STR}/todos")
    data = response.json()

    # Then
    assert response.status_code == 200
    assert data == [{"todo": 1}, {"todo": 2}]


def test_fetch_todo(client):
    # When
    response = client.get(f"{settings.API_V1_STR}/todos/1")
    data = response.json()

    # Then
    assert response.status_code == 200
    assert data == {"todo": "1"}
