import os
from mongoengine import connect
from settings import MONGO_CONNECTION_HOST, MONGO_CONNECTION_NAME, \
                     MONGO_MOCKED_CONNECTION_HOST


def get_connection_url():
    if os.environ.get('IS_TEST') == '1':
        return MONGO_MOCKED_CONNECTION_HOST
    else:
        return MONGO_CONNECTION_HOST


connection = connect(MONGO_CONNECTION_NAME,
                     host=get_connection_url())


