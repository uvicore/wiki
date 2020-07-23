import uvicore
from uvicore import log
from uvicore.contracts import Application, Package
from uvicore.support.provider import ServiceProvider


class Wiki(ServiceProvider):

    def register(self, app: Application) -> None:
        log('wiki provider.register()')
        """Register package into uvicore framework.
        All packages are registered before the framework boots.  This is where
        you define your packages configs and IoC bindings.  Configs are deep merged only after
        all packages are registered.  No real work should be performed here as it
        is very early in the bootstraping process and most internal processes are not
        instantiated yet.
        """
        # Register configs
        # If config key already exists items will be deep merged allowing
        # you to override small peices of other package configs
        self.configs([
            # This package (prefix must match your config.app.py config_prefix)
            {'key': 'mreschke.wiki', 'module': 'mreschke.wiki.config.wiki.config'},

            # Foundation exists, so this is a deep merge override
            {'key': 'uvicore.foundation', 'module': 'mreschke.wiki.config.uvicore.foundation.config'},
        ])

    def boot(self, app: Application, package: Package) -> None:
        log('wiki provider.boot()')
        """Bootstrap package into uvicore framework.
        Boot takes place after all packages are registered.  This means all package
        configs are deep merged to provide a complete and accurate view of all configs.
        This is where you load views, assets, routes, commands...
        """
        # Define view and asset paths and configure the templating system
        self.load_views(app, package)

        # Define Web and API routers
        self.load_routes(app, package)

        # Define CLI commands to be added to the ./uvicore command line interface
        self.load_commands(app, package)

    def load_views(self, app: Application, package: Package) -> None:
        """Define view and asset paths and configure the templating system
        """
        # Add view paths
        self.views(package, ['mreschke.wiki.http.views'])

        # Add asset paths
        self.assets(package, [
            'mreschke.wiki.http.static2',  #foundation example - BLUE
            'mreschke.wiki.http.static',     # wiki override example - RED
        ])

        def url_method(context: dict, name: str, **path_params: any) -> str:
            request = context["request"]
            return request.url_for(name, **path_params)

        def up_filter(input):
            return input.upper()

        def up_filter2(context, input):
            return input.upper()

        def is_prime(n):
            import math
            if n == 2:
                return True
            for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
                if n % i == 0:
                    return False
            return True

        # Add custom template options
        self.template(package, {
            'context_functions': [
                {'name': 'url2', 'method': url_method}
            ],
            'context_filters': [
                {'name': 'up', 'method': up_filter2}
            ],
            'filters': [
                {'name': 'up', 'method': up_filter}
            ],
            'tests': [
                {'name': 'prime', 'method': is_prime}
            ],
        })
        # Optionally, hack jinja to add anything possible like so
        #app.jinja.env.globals['whatever'] = somefunc




    def load_routes(self, app: Application, package: Package) -> None:
        """Define Web and API router
        """
        self.web_routes(package, 'mreschke.wiki.http.routes.web.Web')
        self.api_routes(package, 'mreschke.wiki.http.routes.api.API')

        # Debug
        # if app.is_http:
        #     app.dump("----start")
        #     for route in app.http.server.routes:
        #         app.dump(route.path)
        #     app.dump("----end")
        #     #app.dd('x')

    def load_commands(self, app: Application, package: Package) -> None:
        """Define CLI commands to be added to the ./uvicore command line interface
        """
        self.commands(package, [
            {
                'group': {
                    'name': 'wiki',
                    'parent': 'root',
                    'help': 'Wiki Commands',
                },
                'commands': [
                    {'name': 'test', 'module': 'mreschke.wiki.commands.test.cli'},
                ],
            },
            {
                'group': {
                    'name': 'db',
                    'parent': 'wiki',
                    'help': 'Wiki DB Commands',
                },
                'commands': [
                    {'name': 'create', 'module': 'mreschke.wiki.commands.db.create'},
                    {'name': 'drop', 'module': 'mreschke.wiki.commands.db.drop'},
                    {'name': 'recreate', 'module': 'mreschke.wiki.commands.db.recreate'},
                    {'name': 'seed', 'module': 'mreschke.wiki.commands.db.seed'},
                ],
            }
        ])
