from apistar import Route
from .views import astrologer_root, astrologer_sign, sign_view, welcome, python_pizza_2018

routes = [
    Route('/', 'GET', welcome),
    Route('/pythonpizza2018', 'GET', python_pizza_2018),
    Route('/{astrologer}', 'GET', astrologer_root),
    Route('/{astrologer}/{sign}', 'GET', astrologer_sign),
    Route('/{astrologer}/{sign}/{kind}', 'GET', sign_view),
]
