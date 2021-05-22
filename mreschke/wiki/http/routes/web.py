import uvicore
from uvicore.http.routing import Routes, WebRouter


@uvicore.routes()
class Web(Routes):

    # Apply scopes to all routes and children controllers
    #scopes = ['authenticated', 'employee']

    def register(self, route: WebRouter):
        """Register Web Route Endpoints"""

        # Define controller base path
        route.controllers = 'mreschke.wiki.http.controllers'

        route.controller('home')
        route.controller('about')

        # Return router
        return route
