from apistar.test import TestClient
from app import app
from src.views import generic_view


def test_hello_world():
    client = TestClient(app)
    response = client.get('/virgo/')
    assert response.status_code == 400
    assert response.json() == {"message": "Sorry for virgo there's no results"}
