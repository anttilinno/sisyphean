
def test_status(client):
    # When
    response = client.get("/")
    data = response.json()

    # Then
    assert response.status_code == 200
    assert data == {"status": "ok"}
