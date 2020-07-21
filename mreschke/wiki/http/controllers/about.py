from uvicore.http import Request, WebRouter, response
from uvicore.support.dumper import dd, dump

route = WebRouter()

@route.get('/about', 'about')
async def about(request: Request):
    # Example Jinja2 Template
    return response.View('wiki/about.j2', {'request': request})

    # Other example responses
    #return response.Text('Text Here')
    #return response.HTML('<b>HTML</b> here')
    #return response.JSON({'json':'here'})
    #return response.UJSON({'json':'here'}) # requiest ujson dependency
    # and more ...


@route.get('/about2')
async def about2(request):
    #return PlainTextResponse('About2')
    return templates.TemplateResponse('wiki/about.j2', {'request': request})
