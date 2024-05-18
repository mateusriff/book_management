from fastapi.testclient import TestClient
from book_management.main import app

client = TestClient(app)


def test_create_book(test_client: TestClient):
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "description": "Test Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"
    assert data["description"] == "Test Description"
    assert "id" in data


def test_read_book(test_client: TestClient):
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "description": "Test Description"},
    )
    book_id = response.json()["id"]

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"
    assert data["description"] == "Test Description"
    assert data["id"] == book_id


def test_update_book(test_client: TestClient):
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "description": "Test Description"},
    )
    book_id = response.json()["id"]

    response = client.put(
        f"/books/{book_id}",
        json={"title": "Updated Test Book", "author": "Updated Test Author", "description": "Updated Test Description"}
    )
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Updated Test Book"
    assert data["author"] == "Updated Test Author"
    assert data["description"] == "Updated Test Description"
    assert data["id"] == book_id


def test_delete_book(test_client: TestClient):
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "description": "Test Description"},
    )
    book_id = response.json()["id"]

    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 404

