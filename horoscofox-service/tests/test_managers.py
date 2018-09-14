from src.managers.astrologer import AstrologerManager as AMMock
from horoscofox import paolo, branko
from datetime import datetime
from src.managers.date import DateManager


def test_get_astrologer_uid(mocker):
    assert AMMock.get_astrologer_uid('fox') == 'FOX'
    assert AMMock.get_astrologer_uid('paolofox') == 'FOX'
    assert AMMock.get_astrologer_uid('paolo') == 'FOX'
    assert AMMock.get_astrologer_uid('branko') == 'BKO'


def test_get_astrologer(mocker):
    assert AMMock.get_astrologer('fox') == paolo
    assert AMMock.get_astrologer('paolofox') == paolo
    assert AMMock.get_astrologer('paolo') == paolo
    assert AMMock.get_astrologer('branko') == branko


def test_is_valid_astrologer(mocker):
    assert AMMock.is_valid_astrologer('fox')
    assert AMMock.is_valid_astrologer('paolofox')
    assert AMMock.is_valid_astrologer('paolo')
    assert AMMock.is_valid_astrologer('branko')
    assert not AMMock.is_valid_astrologer('mymom')


def test_get_date(mocker):
    date_arr = [datetime(2018, 5, 27, 0, 0).date(),
                datetime(2018, 5, 28, 0, 0).date()]
    mocker.patch('src.managers.DateManager.today', date_arr[0])
    mocker.patch('src.managers.DateManager.tomorrow', date_arr[1])

    assert DateManager.reset(date_arr[0]) == datetime(2018, 5, 27, 0, 0)
