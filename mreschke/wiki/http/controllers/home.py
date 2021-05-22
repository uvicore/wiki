import uvicore
from uvicore.http import Request, response
from uvicore.http.routing import WebRouter, Controller


@uvicore.controller()
class Home(Controller):

    def register(self, route: WebRouter):

        @route.get('/', name='home')
        async def home(request: Request):
            return response.View('wiki/home.j2', {
                'request': request
            })

        # Return router
        return route



