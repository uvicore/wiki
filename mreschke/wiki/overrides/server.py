from uvicore.http.server import _Server


class Server(_Server):
    def __init__(self, debug: bool, title: str, version: str, openapi_url: str, docs_url: str, redoc_url: str):
        print('##### My Custom HTTP Server Override #####')
        super().__init__(debug, title, version, openapi_url, docs_url, redoc_url)
