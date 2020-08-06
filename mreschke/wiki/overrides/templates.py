from uvicore.http.templating.jinja import _Jinja


class Templates(_Jinja):
    def __init__(self):
        print('##### My Custom Templates Override #####')
        super().__init__()
