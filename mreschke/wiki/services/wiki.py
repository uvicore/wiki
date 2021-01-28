import uvicore
from uvicore.package import ServiceProvider
from uvicore.http.provider import Http
from uvicore.database.provider import Db
from uvicore.console.provider import Cli
from uvicore.support.dumper import dump, dd


@uvicore.provider()
class Wiki(ServiceProvider, Cli, Db, Http):

    def register(self) -> None:
        """Register package into the uvicore framework.
        All packages are registered before the framework boots.  This is where
        you define your packages configs, IoC bindings and early event listeners.
        Configs are deep merged only after all packages are registered.  No real
        work should be performed here as it is very early in the bootstraping
        process and we have no clear view of the full configuration system."""

        # Register configs
        # If config key already exists items will be deep merged allowing
        # you to override granular aspects of other package configs
        self.configs([
            # Here self.name is your packages name (ie: mreschke.wiki).
            {'key': self.name, 'module': 'mreschke.wiki.config.package.config'},
            {'key': self.name, 'module': 'mreschke.wiki.config.database.config'},

            # Foundation exists, so this is a deep merge override
            #{'key': 'uvicore.foundation', 'module': 'mreschke.wiki.config.uvicore.foundation.config'},

            # Auth exists, so this is a deep merge override
            {'key': 'uvicore.auth', 'module': 'mreschke.wiki.config.uvicore.auth.config'},
        ])

    def boot(self) -> None:
        """Bootstrap package into the uvicore framework.
        Boot takes place after ALL packages are registered.  This means all package
        configs are deep merged to provide a complete and accurate view of all
        configuration. This is where you register, connections, models,
        views, assets, routes, commands...  If you need to perform work after ALL
        packages have booted, use the event system and listen to the booted event:
        self.events.listen('uvicore.foundation.events.app.Booted, self.booted')"""

        # Define Service Provider Registrations
        self.registers(self.package.config.registers)

        # Define Database Connections
        self.connections(
            config=self.package.config.database.connections,
            default=self.package.config.database.default
        )

        self.package.database.connections[0].dia

        # Define all tables or models
        # The goal is to load up all SQLAlchemy tables for complete metedata definitions.
        # If you separate tables vs models use self.tables(['myapp.database.tables.*])
        # If you use models only, or models with inline tables then use self.models(['myapp.models.*])
        # Order does not matter as they are sorted topologically for ForeignKey dependencies
        self.models([
            'mreschke.wiki.models',
        ])
        #from mreschke.wiki.database import tables
        #self.tables([
            #'mreschke.wiki.database.tables.*',
            #'uvicore.auth.database.tables.*',
        #])

        # Define database seeders
        self.seeders([
            #'uvicore.auth.database.seeders.seeders.seed',
            'mreschke.wiki.database.seeders.seed',
        ])

        # Define view and asset paths and configure the templating system
        self.define_views()

        # Define Web and API routers
        self.define_routes()

        # Define CLI commands to be added to the ./uvicore command line interface
        self.define_commands()

    def define_views(self) -> None:
        """Define view and asset paths and configure the templating system"""

        # Define view paths
        self.views(['mreschke.wiki.http.views'])

        # Define public paths
        self.public(['mreschke.wiki.http.public'])

        # Define asset paths
        self.assets(['mreschke.wiki.http.public.assets'])

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

        # Define custom template options
        self.template({
            'context_functions': {
                'url2': url_method,
            },
            'context_filters': {
                'up': up_filter2,
            },
            'filters': {
                'up': up_filter,
            },
            'tests': {
                'prime': is_prime,
            },
        })
        # Optionally, hack jinja to add anything possible like so
        #app.jinja.env.globals['whatever'] = somefunc

    def define_routes(self) -> None:
        """Define Web and API prefix and routers"""
        self.web_routes(
            module='mreschke.wiki.http.routes.web.Web',
            prefix=self.package.config.route.web_prefix
        )
        self.api_routes(
            module='mreschke.wiki.http.routes.api.Api',
            prefix=self.package.config.route.api_prefix
        )

    def define_commands(self) -> None:
        """Define CLI commands to be added to the ./uvicore command line interface"""

        self.commands({
            'wiki': {
                'help': 'Wiki Commands',
                'commands': {
                    'test': 'mreschke.wiki.commands.test.cli',
                }
            },

            'wiki:deep': {
                'help': 'Deep group',
                'commands': {
                    'test': 'mreschke.wiki.commands.test.cli',
                }
            }
        })


        # group = 'wiki'
        # self.commands([
        #     {
        #         'group': {
        #             'name': group,
        #             'parent': 'root',
        #             'help': 'Wiki Commands',
        #         },
        #         'commands': [
        #             {'name': 'test', 'module': 'mreschke.wiki.commands.test.cli'},
        #         ],
        #     },




        # was commented
            # {
            #     'group': {
            #         'name': 'db',
            #         'parent': group,
            #         'help': 'Wiki DB Commands',
            #     },
            #     'commands': [
            #         {'name': 'create', 'module': 'mreschke.wiki.commands.db.create'},
            #         {'name': 'drop', 'module': 'mreschke.wiki.commands.db.drop'},
            #         {'name': 'recreate', 'module': 'mreschke.wiki.commands.db.recreate'},
            #         {'name': 'seed', 'module': 'mreschke.wiki.commands.db.seed'},
            #     ],
            # }
        # ])
