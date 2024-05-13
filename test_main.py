from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_intersect_segments():
    # Test case where there are no intersecting rectangles
    response = client.post("/intersect/", json={"x1": 5, "y1": 5, "x2": 6, "y2": 6})
    assert response.status_code == 200

    assert response.json() == []

    # Test case where there is one intersecting rectangle

    # Test case where there are multiple intersecting rectangles
    response = client.post("/intersect/", json={"x1": 0, "y1": 0, "x2": 2, "y2": 2})
    assert response.status_code == 200
    assert len(response.json()) > 1

    # Test case where all rectangles intersect
    response = client.post("/intersect/", json={"x1": 0, "y1": 0, "x2": 4, "y2": 4})
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.post("/intersect/", json={"x1": 1, "y1": 1, "x2": 3, "y2": 3})
    assert response.status_code == 200
    print(response.json())
    assert len(response.json()) == 3

    # Test case where invalid data is provided
    response = client.post(
        "/intersect/", json={"x1": "a", "y1": "b", "x2": "c", "y2": "d"}
    )
    assert response.status_code == 422
