import uvicore
from uvicore.http.routing import Routes, ApiRouter, ModelRouter


@uvicore.routes()
class Api(Routes):

    # Apply scopes to all routes and children controllers
    #scopes = ['authenticated', 'employee']

    def register(self, route: ApiRouter):
        """Register API Route Endpoints"""

        # Define controller base path
        route.controllers = 'mreschke.wiki.http.api'

        # Include dynamic model CRUD API endpoints (the "auto API")!
        #@route.group()
        #def autoapi():
        #def autoapi(scopes=['authenticated']):
            #route.include(ModelRouter)

        route.controller('post', tags=['Post'])

        # Return router
        return route
