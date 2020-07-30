from uvicore.foundation.application import _Application


class Application(_Application):
    def __init__(self):
        print('##### My Custom Application Override #####')
        super().__init__()
