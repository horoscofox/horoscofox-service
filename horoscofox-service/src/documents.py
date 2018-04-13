import connection
import datetime
from mongoengine import *

SIZE = (('BKO', 'Branko'),
        ('FOX', 'Paolo Fox'),
        )


class Horoscope(Document):
    text = StringField(max_length=None, min_length=None, required=True)
    date_start = DateTimeField(required=False)
    date_end = DateTimeField(required=False)
    sign = StringField(max_length=15, required=True)
    astrologer = StringField(max_length=3, required=True, choices=SIZE)
    meta = {
        'ordering': ['-date_start']
    }
