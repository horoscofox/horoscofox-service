from horoscofox.errors import AstrologerException
from documents import Horoscope
from apistar import http
from utils import (fromDocToJson)
from managers import AstrologerManager as AManager, DateManager as DManager

DEFAULT_FIELDS_JSON = ['text', 'date_start', 'date_end']


async def astrologer_root(astrologer: str) -> http.JSONResponse:
    if AManager.is_valid_astrologer(astrologer):
        data = {'message': "Sorry but " +
                astrologer + " is away at the moment"}
    else:
        data = {'message': "No astrologer accepted!"}
    return http.JSONResponse(data, status_code=400)


async def astrologer_sign(astrologer: str, sign: str) -> http.JSONResponse:
    if AManager.is_valid_astrologer(astrologer):
        data = {'message': "Sorry but there is currently no horoscope of the " +
                sign+" readed by "+astrologer}
    else:
        data = {'message': "No astrologer accepted!"}
    return http.JSONResponse(data, status_code=400)


async def sign_view(astrologer: str, sign: str, kind: str) -> http.JSONResponse:
    if not AManager.is_valid_astrologer(astrologer):
        return http.JSONResponse({'message': "No astrologer accepted!"},
                                 status_code=400)
    if not AManager.is_valid_sign(sign):
        return http.JSONResponse({'message': sign + " is not valid"},
                                 status_code=400)

    astrologer_module = AManager.get_astrologer(astrologer)
    astr_uid = AManager.get_astrologer_uid(astrologer)
    try:
        horoscope = Horoscope.objects.get(sign=sign,
                                          astrologer=astr_uid,
                                          date_start=DManager.get_date(kind))
        horoscope_jsn = fromDocToJson(horoscope, DEFAULT_FIELDS_JSON)
        data = {'message': horoscope_jsn}
        return http.JSONResponse(data, status_code=200)
    except Exception as ex:
        print(ex)
        astro_api = astrologer_module.get(sign, kind)
        mid_date_start = DManager.reset(astro_api.date_start)
        mid_date_end = DManager.reset(astro_api.date_end)
        horoscope = Horoscope(text=astro_api.text,
                              date_start=mid_date_start,
                              sign=sign, astrologer=astr_uid,
                              date_end=mid_date_end)
        horoscope.save()
        data = {'message': astro_api.json()}
        return http.JSONResponse(data, status_code=201)
