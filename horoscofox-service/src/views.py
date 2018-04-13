from horoscofox import paolo, branko
from horoscofox.errors import AstrologerException
from documents import Horoscope
import logger
from apistar import http
from utils import astrologer_modules, resetToMidnight, getDateStart

# Private methods
def _checkAstrologer(astrologer):
    try:
        astrologer_module = astrologer_modules[astrologer][1]
        return True
    except Exception as ex:
        return False


async def astrologer_root(astrologer: str) -> http.JSONResponse:
    if _checkAstrologer(astrologer):
        data = {'message': "Sorry but " +
                astrologer + " is away at the moment"}
    else:
        data = {'message': "No astrologer accepted"}
    return http.JSONResponse(data, status_code=400)


async def astrologer_sign(astrologer: str, sign: str) -> http.JSONResponse:
    if _checkAstrologer(astrologer):
        data = {'message': "Sorry but there is currently no horoscope of the " +
                sign+" readed by "+astrologer}
    else:
        data = {'message': "No astrologer accepted"}
    return http.JSONResponse(data, status_code=400)


async def sign_view(astrologer: str, sign: str, kind: str) -> http.JSONResponse:
    if not _checkAstrologer(astrologer):
        return http.JSONResponse({'message': "No astrologer accepted"}, status_code=400)
    
    astrologer_module = astrologer_modules[astrologer][1]
    astrologer_cut = astrologer_modules[astrologer][0]
    try:
        horoscope = Horoscope.objects.get(sign=sign,
                                          astrologer=astrologer_cut).json()
        data = {'message': horoscope}
        return http.JSONResponse(data, status_code=200)
    except Exception as ex:
        horo_api_resp = astrologer_module.get(sign, kind)
        horoscope = Horoscope(text=horo_api_resp.text,
                              date_start=getDateStart(kind),
                              sign=sign, astrologer=astrologer_cut)
        horoscope.date_start = resetToMidnight(horo_api_resp.date_start)
        horoscope.date_end = resetToMidnight(horo_api_resp.date_end)
        horoscope.save()
        data = {'message': horo_api_resp.json()}
        return http.JSONResponse(data, status_code=201)
