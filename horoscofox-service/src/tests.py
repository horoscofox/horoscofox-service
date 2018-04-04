from apistar.test import TestClient
from src.views import generic_view


def test_generic_view():
    test_sign = "virgo"
    data = generic_view(sign=test_sign)
    assert data == {'message': "Sorry for virgo there's no results"}
