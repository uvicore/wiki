from uvicore.http.routing.web_router import _WebRouter


class WebRouter(_WebRouter):
    def __init__(self):
        print('##### My Custom WebRouter Override #####')
        super().__init__()
