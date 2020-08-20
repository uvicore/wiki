from uvicore.package.provider import _ServiceProvider


class ServiceProvider(_ServiceProvider):
    def __init__(self, app, package, app_config, package_config) -> None:
        print('##### My Custom ServiceProvider Override #####')
        super().__init__(app, package, app_config, package_config)
