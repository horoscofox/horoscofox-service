from apistar import test
from app import app
from documents import Horoscope
from datetime import datetime
from horoscofox import paolo
from managers import DateManager
from settings import MONGO_MOCKED_CONNECTION_HOST
import pytest


client = test.TestClient(app)


def test_horoscope_exist_in_db(mocker):

    mocked_horoscope = Horoscope(
        text="Non tutte le rose si apriranno sotto il sole",
        date_start=datetime(2018, 4, 22, 0, 0).date(),
        date_end=datetime(2018, 4, 23, 0, 0).date()
    )
    horoscope_get = mocker.patch('views.Horoscope')
    horoscope_get.objects.get.return_value = mocked_horoscope
    response = client.get('/fox/leo/today')

    assert response.json() == {
        "message": {
            "text": "Non tutte le rose si apriranno sotto il sole",
            "date_start": "2018-04-22",
            "date_end":	"2018-04-23"
        }}
    paolo_get = mocker.patch('horoscofox.paolo')
    paolo_get.get.assert_not_called()


def test_horoscope_not_exist_in_db(mocker):

    mocked_horoscope = {
        "text": "Sole positivo nel tuo segno, amore e soldi",
        "date_start": "2018-05-27",
        "date_end":	"2018-05-28"
    }
    date_arr = [datetime(2018, 5, 27, 0, 0).date(),
                datetime(2018, 5, 28, 0, 0).date()]
    # Let's patch
    mocked_astrologer = mocker.patch.object(paolo, 'get')
    mocked_collection = mocker.patch('views.Horoscope')
    resetter = mocker.patch('views.DManager')

    # return values are now mocked
    mocked_astrologer.return_value.text = mocked_horoscope['text']
    mocked_astrologer.return_value.date_start = date_arr[0]
    mocked_astrologer.return_value.date_end = date_arr[1]
    mocked_astrologer.return_value.json.return_value = mocked_horoscope

    resetter.today = date_arr[0]
    resetter.tomorrow = date_arr[1]

    # Visit url
    response = client.get('/fox/scorpio/today')

    # Asserts
    assert response.json() == {
        "message": {
            "text": "Sole positivo nel tuo segno, amore e soldi",
            "date_start": "2018-05-27",
            "date_end":	"2018-05-28"
        }}

    mocked_astrologer.assert_called_once_with('scorpio', 'today')
    resetter.reset.assert_any_call(date_arr[0])
    resetter.reset.assert_any_call(date_arr[1])
    mocked_collection.objects.get.assert_called()
    with pytest.raises(Exception) as excinfo:
        Horoscope.objects.get(sign='scorpio',
                              astrologer='FOX',
                              date_start=datetime(2018, 5, 27, 0, 0).date())

    mocked_collection.return_value.save.assert_called()
