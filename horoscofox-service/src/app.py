from urls import routes
from apistar.frameworks.asyncio import ASyncIOApp as App
from apistar.backends import django_orm
from settings import settings


app = App(
    routes=routes,
    settings=settings,
    commands=django_orm.commands,  # Install custom commands.
    components=django_orm.components  # Install custom components.
)

if __name__ == '__main__':
    app.main()
