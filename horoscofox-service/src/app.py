from __future__ import absolute_import
from .urls import routes
from .settings import (DEV_SERVER_ADDR, DEV_SERVER_PORT,
                      DEV_USE_DEBUGGER, DEV_USE_RELOADER)
from apistar import App
from apistar_cors_hooks import CORSRequestHooks

custom_options = {"origin": "*"}
event_hooks = [CORSRequestHooks(options=custom_options)]
app = App(routes=routes, event_hooks=event_hooks)


if __name__ == '__main__':
    app.serve(DEV_SERVER_ADDR, DEV_SERVER_PORT,
              use_debugger=DEV_USE_DEBUGGER, use_reloader=DEV_USE_RELOADER)
