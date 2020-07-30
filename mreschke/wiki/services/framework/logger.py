import logging
from uvicore.logging.logger import _Logger


class Logger(_Logger):
    def __init__(self, config):
        print('##### My Custom Logger Override #####')
        super().__init__(config)

    def info(self, message):
        logging.info('LOG OVERRIDE: ' + str(message))
