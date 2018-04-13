from urls import routes
from apistar import ASyncApp, Route
from settings import DEV_SERVER_ADDR, DEV_SERVER_PORT, DEV_USE_DEBUGGER, DEV_USE_RELOADER
app = ASyncApp(
    routes=routes
)

if __name__ == '__main__':
    app.serve(DEV_SERVER_ADDR, DEV_SERVER_PORT,
              use_debugger=DEV_USE_DEBUGGER, use_reloader=DEV_USE_RELOADER)
