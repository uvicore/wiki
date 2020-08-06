from typing import Generic, List, TypeVar, Union
from uvicore.http.routing.routes import _Routes

# Generic Router (APIRouter or WebRouter)
R = TypeVar('R')


class Routes(_Routes, Generic[R]):
    def __init__(self, app, package, Router, prefix):
        print('##### My Custom Routes Override #####')
        super().__init__(app, package, Router, prefix)
