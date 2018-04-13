from urls import routes
from apistar import ASyncApp, Route

app = ASyncApp(
    routes=routes
)

if __name__ == '__main__':
    app.serve('0.0.0.0', 9001, use_debugger=True, use_reloader=True)
