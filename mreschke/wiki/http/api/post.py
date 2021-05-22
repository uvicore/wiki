import uvicore
from uvicore.typing import List, Optional
from mreschke.wiki import models
from uvicore.http.routing import ApiRouter, Controller
from uvicore.http.exceptions import NotFound

from uvicore.http.routing import Guard


@uvicore.controller()
class Post(Controller):

    # Method 1 (preferred)
    scopes = ['authenticated']

    # Method 2
    #auth = Guard(['authenticated'])

    # Method 3
    # middleware = [
    #     Guard(['authenticated'])
    # ]

    def register(self, route: ApiRouter):

        @route.get('/posts')
        #@route.get('/posts', scopes=['authenticated'])
        async def posts(include: Optional[str] = '') -> List[models.Post]:
            includes = include.split(',') if include else []
            return await models.Post.query().include(*includes).get()

        @route.get('/posts/{id}')
        async def post(id: int, include: Optional[str] = '') -> models.Post:
            includes = include.split(',') if include else []
            result = await models.Post.query().include(*includes).find(id)
            if not result: raise NotFound
            return result

        # Return router
        return route
