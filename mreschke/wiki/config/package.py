from uvicore.typing import OrderedDict

# This is the main wiki config.  All items here can be overridden
# when used inside other applications.  Accessible at config('mreschke.wiki')

config = {

    # --------------------------------------------------------------------------
    # Route Configuration
    # --------------------------------------------------------------------------
    # Or like so, no underscores, so in dot notation config('blog.route.prefix')
    # have to do deep merges
    'route': {
        'web_prefix': '',
        'api_prefix': '/wiki/api',
    },

    # mode?  Standalone, library?
    # If each app comes with a full set of auth tables (user, roles, perm...)
    # But you INCLUDE it as a LIB, it should't make those tables twice
    # Must share the auth system, only uses the HOSTS auth tables
    # Host/guest?  App/Library NO, becuase apps are apps and libraries
    # Package.  Package can be APP or LIB?


    # When you say APP, you don't know if its the host or the guest
    # So cannot say APP MODE
    # Standalone has to have word APP after it, standalone mode or standalone app


    # # --------------------------------------------------------------------------
    # # Database Connections
    # # --------------------------------------------------------------------------
    # 'database': {
    #     'default': 'wiki',
    #     'connections': {
    #         'wiki': {
    #             'driver': 'mysql',
    #             'dialect': 'pymysql',
    #             'host': '127.0.0.1',
    #             'port': 3306,
    #             'database': 'uvicore_wiki',
    #             'username': 'root',
    #             'password': 'techie',
    #             'prefix': None,
    #             #'include_connections': ['auth']
    #         },
    #         # 'some-sql': {
    #         #     'driver': 'mysql',
    #         #     'dialect': 'pymysql',
    #         #     'host': '127.0.0.1',
    #         #     'port': 3306,
    #         #     'database': 'somesql',
    #         #     'username': 'root',
    #         #     'password': 'techie',
    #         #     'prefix': None,
    #         # },
    #     },
    # },


    # --------------------------------------------------------------------------
    # Registration Control
    # --------------------------------------------------------------------------
    # This lets you control the service provider registrations.  If this app
    # is used as a package inside another app you might not want some things
    # registered in that context.  Use config overrides in your app to change
    # registrations
    # 'registers': {
    #     'web_routes': False,
    #     'api_routes': False,
    #     'middleware': False,
    #     'views': False,
    #     'assets': False,
    #     'commands': False,
    #     'models': False,
    #     'tables': False,
    #     'seeders': False,
    # },


    # --------------------------------------------------------------------------
    # Package Dependencies (Service Providers)
    #
    # Define all the packages that this package depends on.  At a minimum, only
    # the uvicore.foundation package is required.  The foundation is very
    # minimal and only depends on configuratino, logging and console itself.
    # You must add other core services built into uvicore only if your package
    # requires them.  Services like uvicore.database, uvicore.orm, uvicore.http
    # uvicore.auth...
    # --------------------------------------------------------------------------
    'dependencies': OrderedDict({
        # Wiki uses database, orm, auth, http
        'uvicore.foundation': {
            'provider': 'uvicore.foundation.services.Foundation',
        },
        'uvicore.database': {
            'provider': 'uvicore.database.services.Database',
        },
        'uvicore.orm': {
            'provider': 'uvicore.orm.services.Orm',
        },
        'uvicore.http': {
            'provider': 'uvicore.http.services.Http',
        },
        'uvicore.auth': {
            'provider': 'uvicore.auth.services.Auth',
        },
    }),

}
