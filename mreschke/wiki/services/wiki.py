import uvicore
from uvicore.package import ServiceProvider
from uvicore.http.provider import Http
from uvicore.database.provider import Db
from uvicore.redis.provider import Redis
from uvicore.console.provider import Cli
from uvicore.support.dumper import dump, dd


@uvicore.provider()
class Wiki(ServiceProvider, Cli, Db, Redis, Http):

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

            # Example of splitting out the app config into multiple files per section
            #{'key': self.name, 'module': 'mreschke.wiki.config.database.config'},

            # Auth exists, so this is a deep merge override
            #{'key': 'uvicore.auth', 'module': 'mreschke.wiki.config.overrides.auth.config'},
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
            connections=self.package.config.database.connections,
            default=self.package.config.database.default
        )

        # Define Redis Connections
        self.redis_connections(
            connections=self.package.config.redis.connections,
            default=self.package.config.redis.default
        )

        # Define all tables or models
        # The goal is to load up all SQLAlchemy tables for complete metedata definitions.
        # If you separate tables vs models use self.tables(['myapp.database.tables])
        # If you use models only, or models with inline tables then use self.models(['myapp.models])
        # Order does not matter as they are sorted topologically for ForeignKey dependencies
        # If you don't have an __init__.py index in your tables or models you can use
        # wildcard imports self.models(['myapp.models.*])
        self.models([
            'mreschke.wiki.models',
        ])
        # self.tables([
        #     'mreschke.wiki.database.tables',
        # ])

        # Define data seeders
        self.seeders([
            'mreschke.wiki.database.seeders.seed',
        ])

        # Define view and asset paths and configure the templating system
        self.define_views()

        # Define Web and API routes and prefixes
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

    def define_routes(self) -> None:
        """Define Web and API routes and prefixes"""

        # Define web routes
        self.web_routes(
            module='mreschke.wiki.http.routes.web.Web',
            prefix=self.package.config.web.prefix,
            #name_prefix=None,
        )

        # Define api routes
        self.api_routes(
            module='mreschke.wiki.http.routes.api.Api',
            prefix=self.package.config.api.prefix,
            #name_prefix='api',
        )

    def define_commands(self) -> None:
        """Define CLI commands to be added to the ./uvicore command line interface"""

        self.commands(
            group='wiki',
            help='Wiki Commands',
            commands={
                'test': 'mreschke.wiki.commands.test.cli',
                'passwd': 'mreschke.wiki.commands.passwd.cli',
            }
        )
