from app import app
from apistar import test

client = test.TestClient(app)


def test_no_sign_no_kind():
    response = client.get('/branko')
    assert response.status_code == 400
    assert response.json() == {
        "message": "Sorry but branko is away at the moment"}

    response = client.get('/mymom')
    assert response.status_code == 400
    assert response.json() == {
        "message": "No astrologer accepted!"}


def test_no_kind():
    response = client.get('/paolo/virgo')
    assert response.status_code == 400
    assert response.json() == {
        "message": "Sorry but there is currently no horoscope of the virgo readed by paolo"}
    response = client.get('/mymom/leo')
    assert response.status_code == 400
    assert response.json() == {
        "message": "No astrologer accepted!"}


def test_no_astrologer_or_sign():
    response = client.get('/paolo/vergine/today')
    assert response.status_code == 400
    assert response.json() == {
        "message": "vergine is not valid"}
    response = client.get('/mymom/leo/today')
    assert response.status_code == 400
    assert response.json() == {
        "message": "No astrologer accepted!"}
