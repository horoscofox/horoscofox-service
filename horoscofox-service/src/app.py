from urls import routes
from apistar.frameworks.asyncio import ASyncIOApp as App

app = App(
    routes=routes
)

if __name__ == '__main__':
    app.main()
