from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls
from views import astrologer_root, astrologer_sign, sign_view

routes = [
    Route('/{astrologer}', 'GET', astrologer_root),
    Route('/{astrologer}/{sign}', 'GET', astrologer_sign),
    Route('/{astrologer}/{sign}/{kind}', 'GET', sign_view),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
