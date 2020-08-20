from typing import List

from mreschke.wiki.models.user import User
from uvicore.http.routing import ApiRouter

route = ApiRouter()

#@route.get('/users', response_model=List[User], include_in_schema=False)
@route.get('/users', response_model=List[User])
async def users():
    #return {'endpoint': 'users'}
    # Fake user as DB is not working yet
    return User.all()
    # return [
    #     {
    #         "id": 1,
    #         "name": "Matthew"
    #     },
    #     {
    #         "id": 2,
    #         "name": "Taylor"
    #     },
    # ]
    #rows = await User.all()
    #return rows


@route.get('/users/{id}', response_model=User)
async def user(id: int):
    # Fake user as DB is not working yet
    return {
        "id": id,
        "name": "Matthew"
    }
