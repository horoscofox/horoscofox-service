from datetime import datetime, timedelta, date
from horoscofox import paolo, branko
from horoscofox.constants import SIGNS

# Costants
FOX_VAL = 'FOX'
BKO_VAL = "BKO"


class AstrologerManager(object):

    __astrologer_modules = {
        'fox': (FOX_VAL, paolo),
        'paolo': (FOX_VAL, paolo),
        'paolofox': (FOX_VAL, paolo),
        'branko': (BKO_VAL, branko)
    }

    @staticmethod
    def get_astrologer(key):
        return AstrologerManager.__astrologer_modules[key][1]

    @staticmethod
    def get_astrologer_uid(key):
        return AstrologerManager.__astrologer_modules[key][0]

    @staticmethod
    def is_valid_astrologer(key):
        try:
            astrologer_module = AstrologerManager.__astrologer_modules[key][1]
            return True
        except Exception as ex:
            return False

    @staticmethod
    def is_valid_sign(key):
        return key in SIGNS


class DateManager(object):
    today = date.today()
    tomorrow = today+timedelta(days=1)

    @staticmethod
    def get_date(kind: str):
        if kind == 'today':
            return DateManager.reset(DateManager.today)
        if kind == 'tomorrow':
            return DateManager.reset(DateManager.tomorrow)

    @staticmethod
    def reset(date):
        return datetime.combine(date, datetime.min.time())
