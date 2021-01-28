from uvicore.http import Request, response, WebRouter
from uvicore.support.dumper import dd, dump

route = WebRouter()

@route.get('/', 'home')
async def home(request: Request):
    return response.View('wiki/home.j2', {'request': request})
