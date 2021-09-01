import uvicore
from uvicore.typing import List, Optional
from mreschke.wiki.models import Post as PostModel
from uvicore.http.routing import ApiRouter, Controller, AutoApi, Guard
from uvicore.http.exceptions import NotFound
from uvicore.http.request import Request
from uvicore.support.dumper import dump, dd


@uvicore.controller()
class Post(Controller):

    # Method 1 (preferred)
    #scopes = ['authenticated']

    # Method 2
    #auth = Guard(['authenticated'])

    # Method 3
    # middleware = [
    #     Guard(['authenticated'])
    # ]

    def register(self, route: ApiRouter):

        # @route.get('/posts')
        # #@route.get('/posts', scopes=['authenticated'])
        # async def posts(include: Optional[str] = '') -> List[models.Post]:
        #     http = uvicore.ioc.make('aiohttp')
        #     includes = include.split(',') if include else []
        #     return await models.Post.query().include(*includes).get()

        # @route.get('/posts/{id}')
        # async def post(id: int, include: Optional[str] = '') -> models.Post:
        #     includes = include.split(',') if include else []
        #     result = await models.Post.query().include(*includes).find(id)
        #     if not result: raise NotFound
        #     return result


        @route.get('/posts/by_topic/{space}/{section}/{topic}', inherits=AutoApi.listsig)
        async def posts_by_space(space: str, section: str, topic: str, **kwargs) -> List[PostModel]:
            """Get all posts in a space/section/topic"""

            # New AutoApi instance
            api = AutoApi[PostModel](PostModel, **kwargs)

            # Start a model ORM query builder based on AutoApi parameters
            query = api.orm_query()

            # Add to the query
            (query.include('topic.section.space')
                .where('topic.slug', '/' + topic)
                .where('topic.section.slug', '/' + section)
                .where('topic.section.space.slug', '/' + space)
            )
            return await query.get()


        @route.get('/posts/by_slug/{space}/{section}/{topic}/{slug}', inherits=AutoApi.getsig)
        async def post_by_slug(space: str, section: str, topic: str, slug: str, **kwargs) -> PostModel:

            # New AutoApi instance
            api = AutoApi[PostModel](PostModel, **kwargs)

            # Start a model ORM query builder based on AutoApi parameters
            query = api.orm_query()

            # Add to the query
            (query.include('topic.section.space')
                .where('topic.slug', '/' + topic)
                .where('topic.section.slug', '/' + section)
                .where('topic.section.space.slug', '/' + space)
                .where('post.slug', slug)
            )
            return await query.get()


        # Return router
        return route
