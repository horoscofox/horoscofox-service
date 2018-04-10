from horoscofox import paolo, branko
from horoscofox.errors import AstrologerException
from documents import Horoscope
import logger
from apistar import Response
from utils import astrologer_modules, resetToMidnight, getDateStart


def astrologer_root(astrologer: str):
    print('addd')
    data = {'message': "Sorry but " + astrologer + " is away at the moment", }
    return Response(data, status=400)


def astrologer_sign(astrologer: str, sign: str):
    data = {'message': "Sorry for " + sign + " there's no results", }
    return Response(data, status=400)


def sign_view(astrologer: str, sign: str, kind: str):
    try:
        astrologer_module = astrologer_modules[astrologer][1]
    except Exception as ex:
        return Response({'message': "No astrologer accepted"}, status=400)

    astrologer_cut = astrologer_modules[astrologer][0]
    try:
        horoscope = Horoscope.objects.get(sign=sign,
                                          astrologer=astrologer_cut).json()
        data = {'message': horoscope}
        return Response(data, status=200)
    except Exception as ex:
        horo_api_resp = astrologer_module.get(sign, kind)
        horoscope = Horoscope(text=horo_api_resp.text,
                              date_start=getDateStart(kind),
                              sign=sign, astrologer=astrologer_cut)
        horoscope.date_start = resetToMidnight(horo_api_resp.date_start)
        horoscope.date_end = resetToMidnight(horo_api_resp.date_end)
        horoscope.save()
        data = {'message': horo_api_resp.json()}
        return Response(data, status=201)


# Custom Private methods
