from uvicore.configuration.configuration import _Configuration


class Configuration(_Configuration):
    def __init__(self):
        print('##### My Custom Configuration Override #####')
        super().__init__()
