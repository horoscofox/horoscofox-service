import connection
import datetime
import os
from mongoengine import connect
from settings import (MONGO_CONNECTION_HOST,
                      MONGO_CONNECTION_NAME,
                      MONGO_MOCKED_CONNECTION_HOST)

ASTROLOGER_UID = (('BKO', 'Branko'),
                  ('FOX', 'Paolo Fox'),
                  )


def get_connection_url():
    if os.environ.get('IS_TEST') == '1':
        return MONGO_MOCKED_CONNECTION_HOST
    else:
        return MONGO_CONNECTION_HOST


connection = connect(MONGO_CONNECTION_NAME,
                     host=get_connection_url())


class Horoscope(Document):
    text = StringField(max_length=None, min_length=None, required=True)
    date_start = DateTimeField(required=False)
    date_end = DateTimeField(required=False)
    sign = StringField(max_length=15, required=True)
    astrologer = StringField(
        max_length=3, required=True, choices=ASTROLOGER_UID)
    meta = {
        'ordering': ['-date_start']
    }


def fromDocToJson(document, arguments):
    res = {}
    for arg in arguments:
        if 'date' in arg:
            res[arg] = document[arg].isoformat()
        else:
            res[arg] = document[arg]
    return res
