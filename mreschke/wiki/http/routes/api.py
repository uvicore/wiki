import uvicore
from uvicore.http.routing import Routes, ApiRouter, ModelRouter


@uvicore.routes()
class Api(Routes):

    # Apply scopes to all routes and children controllers
    #scopes = ['authenticated']
    #scopes = ['authenticated', 'employee']
    #scopes = None

    # HTTP example
    # TOKEN=$(fa-api tgb-local login wiki-vue-app token)
    # http GET 'https://wiki-api-local.triglobal.io/api/auth/userinfo' Authorization:"Bearer $TOKEN"

    def register(self, route: ApiRouter):
        """Register API Route Endpoints"""

        # Define controller base path
        route.controllers = 'mreschke.wiki.http.api'

        # Include dynamic model CRUD API endpoints (the "auto API")!
        #@route.group(scopes=['authenticated'])
        @route.group()
        def autoapi():
            #route.include(ModelRouter)
            route.include(ModelRouter, options={
                #'scopes': ['autoapi']
                'scopes': []
                # 'scopes': {
                #     'create': ['autoapi.create'],
                #     #'read': ['autoapi.read'],
                #     'update': ['autoapi.update'],
                #     'delete': ['autoapi.delete'],
                # }
            })



        route.controller('post', tags=['Posts'])

        # Return router
        return route
