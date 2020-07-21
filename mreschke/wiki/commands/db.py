import typer
from uvicore import app
from uvicore.support.click import click, group_kargs
from .. import models

create = typer.Typer()
@create.command()
def create_cmd():
    """Unicorn db create
    """
    print('db create here')
    app.db.metadata.create_all(app.db.engine)


drop = typer.Typer()
@drop.command()
def drop_cmd():
    """Unicorn db drop
    """
    print('db drop here')
    app.db.metadata.drop_all(app.db.engine)


recreate = typer.Typer()
@recreate.command()
def recreate_cmd():
    """Unicorn db recreate (drop/create)
    """
    print('db recreate here')
    app.db.metadata.drop_all(app.db.engine)
    app.db.metadata.create_all(app.db.engine)


seed = typer.Typer()
@seed.command()
def seed_cmd():
    """Unicorn db seed (drop/create)
    """
    print('db seed here')
    from ..database.seeders import seed_all
    seed_all()
