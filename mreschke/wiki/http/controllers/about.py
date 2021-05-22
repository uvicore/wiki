import uvicore
from uvicore.http import Request, response
from uvicore.http.routing import WebRouter, Controller


@uvicore.controller()
class About(Controller):

    def register(self, route: WebRouter):

        @route.get('/about', name='about')
        async def home(request: Request):
            return response.View('wiki/about.j2', {
                'request': request
            })

        @route.get('/about2')
        async def about2(request: Request):
            return response.Text('/about2 plain text')

        # Return router
        return route
