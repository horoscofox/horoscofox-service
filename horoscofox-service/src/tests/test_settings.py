import os
import settings
from connection import get_connection_url


MOCK_TEST_URL = "testenviroment://url/database"
MOCK_NO_TEST_URL = "notestenviroment://url/database"


def test_enviroment_variables_false(mocker):
    mocked_env = mocker.patch.dict( 
        'os.environ', {'IS_TEST': '0'}
    )
    mock_settings_var = mocker.patch(
        'connection.MONGO_CONNECTION_HOST', MOCK_NO_TEST_URL)
    assert get_connection_url() == MOCK_NO_TEST_URL


def test_enviroment_variables_true(mocker):
    mocked_env = mocker.patch.dict(
        'os.environ', {'IS_TEST': '1'}
    )
    mock_settings_var = mocker.patch(
        'connection.MONGO_MOCKED_CONNECTION_HOST', MOCK_TEST_URL)
    assert get_connection_url() == MOCK_TEST_URL
