from uvicore import app, config
from uvicore.http import Router, controller
from mreschke.wiki.models.user import User
from typing import List

# New router for this controller
route = Router()



#import sqlalchemy as sa
#from databases import Database
# metadata = sa.MetaData()
# users = sa.Table(
#     "user",
#     metadata,
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column("name", sa.String(length=50))
# )

#database = Database("mysql://root:techie@127.0.0.1/uvicore_wiki")
#await database.connect()


# @app.http.on_event("startup")
# async def startup():
#     await database.connect()

# @app.http.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


# Class based Controller
@controller(route)
class Starlette:

    @route.get('/database', response_model=List[User])
    async def database(self):
        #return {'Page': 'Database'}
        #await database.connect()
        #query = users.select()

        #user = User()
        #query = user.table().select()

        #query = User.table.select()
        #rows = await app.db.fetch_all(query=query)

        # Works ORM
        #rows = await User.find(1)
        rows = await User.all()

        #await database.disconnect()
        return rows

