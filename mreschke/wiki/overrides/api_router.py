from uvicore.http.routing.api_router import _ApiRouter


class ApiRouter(_ApiRouter):
    def __init__(self):
        print('##### My Custom ApiRouter Override #####')
        super().__init__()
