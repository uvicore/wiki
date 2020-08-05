import uvicore
from uvicore import log
from uvicore.support.provider import ServiceProvider
from uvicore.support.dumper import dump, dd


class Wiki(ServiceProvider):

    def register(self) -> None:
        """Register package into uvicore framework.
        All packages are registered before the framework boots.  This is where
        you define your packages configs and IoC bindings.  Configs are deep merged only after
        all packages are registered.  No real work should be performed here as it
        is very early in the bootstraping process and most internal processes are not
        instantiated yet.
        """

        log('wiki provider.register()')

        # Register configs
        # If config key already exists items will be deep merged allowing
        # you to override small peices of other package configs
        self.configs([
            # Here self.name is your packages name (ie: mreschke.wiki).
            {'key': self.name, 'module': 'mreschke.wiki.config.wiki.config'},
            #{'key': self.name, 'module': 'mreschke.wiki.config.database.config'},

            # Foundation exists, so this is a deep merge override
            {'key': 'uvicore.foundation', 'module': 'mreschke.wiki.config.uvicore.foundation.config'},
        ])


        # # Test override logging binding
        # # Register IoC bindings
        # self.bind(
        #     name='Logger',
        #     object='mreschke.wiki.services.logging.Logging',
        #     kwargs={'config': uvicore.config('app.logger')},
        #     singleton=True,
        #     aliases=['Log', 'log', 'logger']
        # )

        # # Set uvicore.log global
        # uvicore.log = uvicore.ioc.make('Logger')


    def boot(self) -> None:
        """Bootstrap package into uvicore framework.
        Boot takes place after all packages are registered.  This means all package
        configs are deep merged to provide a complete and accurate view of all configs.
        This is where you load views, assets, routes, commands...
        """

        log('wiki provider.boot()')

        # Define view and asset paths and configure the templating system
        self.load_views()

        # Define Web and API routers
        self.load_routes()

        # Define CLI commands to be added to the ./uvicore command line interface
        self.load_commands()

    def load_views(self) -> None:
        """Define view and asset paths and configure the templating system
        """
        # Add view paths
        self.views(['mreschke.wiki.http.views'])

        # Add asset paths
        self.assets([
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
        self.template({
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

    def load_routes(self) -> None:
        """Define Web and API router
        """
        self.web_routes('mreschke.wiki.http.routes.web.Web')
        self.api_routes('mreschke.wiki.http.routes.api.API')

        # Debug
        # if app.is_http:
        #     app.dump("----start")
        #     for route in app.http.server.routes:
        #         app.dump(route.path)
        #     app.dump("----end")
        #     #app.dd('x')

    def load_commands(self) -> None:
        """Define CLI commands to be added to the ./uvicore command line interface
        """
        self.commands([
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
