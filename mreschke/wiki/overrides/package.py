#from uvicore.foundation.package import _Package
from uvicore.package.package import _Package


class Package(_Package):
    def config(self, dotkey: str = None):
        print('##### My Custom Package Override #####')
        return super().config(dotkey)
