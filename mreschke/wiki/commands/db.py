from mreschke.wiki import models
from uvicore.auth import models
from uvicore.database.commands.db import create, drop, recreate, seed


# import typer
# from typing import Optional
# from uvicore import app, db
# from uvicore.support.click import click, group_kargs
# from mreschke.wiki import models
# from uvicore.support.dumper import dump, dd

# # Commands
# create = typer.Typer()
# drop = typer.Typer()
# recreate = typer.Typer()
# seed = typer.Typer()

# # Default connection for this app
# #default = 'wiki'

# @create.command()
# def create_cmd(con: Optional[str] = None):
#     """Unicorn db create
#     """
#     print('db create here')
#     #app.db.metadata.create_all(app.db.engine)
#     db.metadata(con).create_all(db.engine(con))

# @drop.command()
# def drop_cmd(con: Optional[str] = None):
#     """Unicorn db drop
#     """
#     print('db drop here')
#     #app.db.metadata.drop_all(app.db.engine)
#     db.metadata(con).drop_all(db.engine(con))

# @recreate.command()
# def recreate_cmd(con: Optional[str] = None):
#     """Unicorn db recreate (drop/create)
#     """
#     print('db recreate here')
#     #app.db.metadata.drop_all(app.db.engine)
#     #app.db.metadata.create_all(app.db.engine)
#     db.metadata(con).drop_all(db.engine(con))
#     db.metadata(con).create_all(db.engine(con))

# @seed.command()
# def seed_cmd(con: Optional[str] = None):
#     """Unicorn db seed (drop/create)
#     """
#     print('db seed here')
#     from mreschke.wiki.database.seeders import seed_all
#     seed_all()
