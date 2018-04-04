from horoscofox import paolo
from horoscofox.errors import PaoloException
from apistar.backends.django_orm import Session

import datetime


def generic_view(session: Session, sign: str):
    try:
        resp = paolo.get(sign=sign)
        return resp.json()
    except Exception as ex:
        return {'message': "Sorry for " + sign + " there's no results"}


def sign_view(session: Session, sign: str, kind: str):

    sign_key = session.Horoscope.get_sign_key(sign)
    try:
        result = session.Horoscope.objects.get(
            date_start=getDateStart(kind), sign=sign_key)
        return {'message': result.text}

    except Exception as ex:
        try:
            horoscope_content = paolo.get(sign, kind).text
        except PaoloException as e2:
            horoscope_content = e2.message
        new_horoscope = session.Horoscope(
            date_start=getDateStart(kind), sign=sign_key, text=horoscope_content)
        new_horoscope.save()

        return {'message': new_horoscope.text}


def getDateStart(kind: str):
    if kind == 'today':
        return datetime.datetime.today().date()
    if kind == 'tomorrow':
        return datetime.datetime.tomorrow()
