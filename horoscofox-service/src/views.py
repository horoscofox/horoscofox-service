from horoscofox.errors import AstrologerException
from apistar import http
from .managers.astrologer import AstrologerManager as AManager
from .managers.date import DateManager as DManager
from .managers.database.dynamodb import Horoscope


def welcome() -> http.JSONResponse:
    data = {
        "project": "Horoscofox",
        'author': {
            "Username": "Owanesh",
            "link": "github.com/Owanesh"
        },
        "contributor": {
            "Username": "astagi",
            "link": "github.com/astagi"
        }
    }
    return http.JSONResponse(data, status_code=200)



def astrologer_root(astrologer: str) -> http.JSONResponse:
    if AManager.is_valid_astrologer(astrologer):
        data = {'message': "ERR0R: Sorry but " +
                astrologer + " is away at the moment"}
    else:
        data = {'message': "ERR0R: No astrologer accepted!"}
    return http.JSONResponse(data, status_code=400)


def astrologer_sign(astrologer: str, sign: str) -> http.JSONResponse:
    if AManager.is_valid_astrologer(astrologer):
        data = {'message': "ERR0R: Sorry but there is currently no horoscope of the " +
                sign + " readed by " + astrologer}
    else:
        data = {'message': "ERR0R: No astrologer accepted!"}
    return http.JSONResponse(data, status_code=400)


def sign_view(astrologer: str, sign: str, kind: str) -> http.JSONResponse:
    horoscope = Horoscope()
    if not AManager.is_valid_astrologer(astrologer):
        return http.JSONResponse({'message': "ERR0R: No astrologer accepted!"},
                                 status_code=400)
    if not AManager.is_valid_sign(sign):
        return http.JSONResponse({'message': "ERR0R: " + sign + " is not valid"},
                                 status_code=400)

    astrologer_module = AManager.get_astrologer(astrologer)
    astr_uid = AManager.get_astrologer_uid(astrologer)
    try:
        search_item = {
            "sign": sign,
            "astrologer": astr_uid,
            "date_start": str(DManager.get_date(kind))
        }

        item = horoscope.get_item(search_item, format='json')

        data = {'message': item}
        print(data)
        return http.JSONResponse(data, status_code=200)
    except Exception as ex:
        print(ex)
        astro_api = astrologer_module.get(sign, kind)
        mid_date_start = DManager.reset(astro_api.date_start)
        mid_date_end = DManager.reset(astro_api.date_end)
        item = {
            "text": astro_api.text,
            "date_start": str(mid_date_start),
            "sign": sign,
            "astrologer": astr_uid,
            "date_end": str(mid_date_end)
        }
        ret = horoscope.insert(item=item)
        data = {'message': astro_api.json()}
        return http.JSONResponse(data, status_code=201)
