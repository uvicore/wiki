from typing import List

from mreschke.wiki.models.post import Post
from uvicore.http.routing import ApiRouter

route = ApiRouter()

#@route.get('/users', response_model=List[User], include_in_schema=False)
@route.get('/posts', response_model=List[Post])
async def posts():
    #return {'endpoint': 'users'}
    # Fake user as DB is not working yet
    return await Post.get()
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


@route.get('/post/{id}', response_model=Post)
async def post(id: int):
    return await Post.find(id)
    # Fake user as DB is not working yet
    # return {
    #     "id":1,
    #     "slug":"bar-million-feeling-provide-third",
    #     "title":"Bar million feeling provide third.",
    #     "creator_id":1,
    #     "creator":None
    # }
