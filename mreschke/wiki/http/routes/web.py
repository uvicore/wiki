from uvicore.http.routing import WebRouter, Routes
from uvicore.support.dumper import dump, dd
from uvicore import app, config


class Web(Routes[WebRouter]):

    endpoints: str = 'mreschke.wiki.http.controllers'

    def register(self):
        # String style
        self.include('about')

        # Import style
        #from mreschke.wiki.http.controllers import about
        #self.include(about.route)




        # Define inline routes
        # from starlette.responses import PlainTextResponse
        # route = self.Router()
        # @route.get('/about')
        # async def about(request):
        #     return PlainTextResponse('About plain text')
        # self.include(route)







        # # Include controller routes
        # self.controller(home)
        # self.controller(about)
        # self.controller(starlette, prefix="/starlette")

        # #app.dd(self.package)

        # # Define inline routes if needed
        # @http.get(prefix + '/hello')
        # async def test():
        #     return {"hello":"world"}



        # from fastapi.responses import HTMLResponse
        # @http.get(prefix + '/about', response_class=HTMLResponse, tags=["asdf"])
        # async def about():
        #     html = "<b>Hi</b> there"
        #     #return HTMLResponse(content=html, status_code=200)
        #     return html


