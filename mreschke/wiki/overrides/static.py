from uvicore.http.static import _StaticFiles


class StaticFiles(_StaticFiles):
    def __init__(self, directories):
        print('##### My Custom StaticFiles Override #####')
        super().__init__(directories)
