from apistar.test import TestClient
from app import app


def test_no_sign_no_kind():
    client = TestClient(app)
    response = client.get('/branko')
    assert response.status_code == 400
    assert response.json() == {"message": "Sorry but branko is away at the moment"}


def test_no_kind():
    client = TestClient(app)
    response = client.get('/paolo/virgo')
    assert response.status_code == 400
    assert response.json() == {"message": "Sorry for virgo there's no results"}
