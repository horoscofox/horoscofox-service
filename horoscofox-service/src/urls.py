from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls
from views import *

routes = [
    Route('/{sign}', 'GET', generic_view),
    Route('/{sign}/{kind}', 'GET', sign_view),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
