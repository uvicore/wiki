import uvicore
from uvicore.http.routing import Routes, ApiRouter, ModelRouter


@uvicore.routes()
class Api(Routes):

    # Apply scopes to all routes and children controllers
    #scopes = ['authenticated']
    #scopes = ['authenticated', 'employee']
    #scopes = None

    def register(self, route: ApiRouter):
        """Register API Route Endpoints"""

        # Define controller base path
        route.controllers = 'mreschke.wiki.http.api'

        # Include dynamic model CRUD API endpoints (the "auto API")!
        @route.group()
        #@route.group(scopes=['x'])  # These scopes are APPENDED to auto api acopes, user must have both
        #def autoapi():
        #def autoapi(scopes=['authenticated']):
        def autoapi():
            # These scopes are used instead of auto api scopes
            route.include(ModelRouter, options={'scopes': []})

            # This sets NO scopes, meaning fully public API
            #route.include(ModelRouter, options={'scopes': []})

            # Use default auto api scopes (posts.read, posts.create...)
            #route.include(ModelRouter)

        #route.controller('post', tags=['Post'])

        # Return router
        return route
