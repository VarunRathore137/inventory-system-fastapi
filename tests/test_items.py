from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_item():
    payload = {
        "name": "Test Item",
        "sku": "TEST123",
        "qty": 10,
        "price": 99.99
    }

    response = client.post("/items", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["sku"] == "TEST123"


def test_list_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert type(response.json()) is list
