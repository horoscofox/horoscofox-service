from datetime import datetime, timedelta, date
from horoscofox import paolo, branko

# Costants
FOX_VAL = 'FOX'
BKO_VAL = "BKO"

astrologer_modules = {
    'fox': (FOX_VAL, paolo),
    'paolo': (FOX_VAL, paolo),
    'paolofox': (FOX_VAL, paolo),
    'branko': (BKO_VAL, branko)
}


def getDateStart(kind: str):
    if kind == 'today':
        d = date.today()
        return resetToMidnight(d)
    if kind == 'tomorrow':
        d = (date.today() + timedelta(days=1))
        return resetToMidnight(d)


def resetToMidnight(date):
    return datetime.combine(date, datetime.min.time())
