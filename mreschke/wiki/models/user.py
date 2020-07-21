# #from uvicore.db import Model, sa
from uvicore import app
from pydantic import BaseModel
import sqlalchemy as sa
from typing import Optional, List, Mapping, TypeVar, Union, Generic
# from mreschke.wiki import db

# class User(db.Model):
#     #__tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(length=50))


# class UserSchema(Schema):
#     id: int
#     name: str

#     class Config:
#         orm_mode = True

E = TypeVar('E')


class Entity(Generic[E], BaseModel):
    @classmethod
    def find(entity: E, id: Union[int,str]) -> E:
        table = entity.Db.table
        query = table.select().where(table.c.id == id)
        return app.db.fetchone(entity, query)

    @classmethod
    def all(entity: E) -> List[E]:
        table = entity.Db.table
        query = table.select()
        return app.db.fetchall(entity, query)

    #.save()

    #@classmethod
    #def create(entity: E, List[E]):



class User(Entity):
    id: Optional[int]
    name: str

    def hi(self):
        return "Hi " + str(self.name)

    class Db:
        # SQLAlchemy Table
        #metadata = sa.MetaData()

        # Because the db config is in the wiki package I also
        # need to know the actual package
        # so package + which connection, if no connection, use default
        package = app.package('wiki')
        connection = 'wiki'  # or blank for default

        # We must be able to use the db without a Model
        # Even without a table definition.  Imagine connecting to some random
        # database, you don't have a Model or a sa.Table(), you just want to query it
        # based on a connection. Preferably with the query builder AND raw
        #db.select(table)
        #db.con('wiki').select(table)

        schema = sa.Table(
            "user",
            app.db.metadata,
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("name", sa.String(length=50))
        )
