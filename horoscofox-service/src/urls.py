from apistar import Route
from .views import astrologer_root, astrologer_sign, sign_view, welcome, pythonpizza

routes = [
    Route('/', 'GET', welcome),
    Route('/{astrologer}', 'GET', astrologer_root),
    Route('/{astrologer}/{sign}', 'GET', astrologer_sign),
    Route('/{astrologer}/{sign}/{kind}', 'GET', sign_view),
]
