from uvicore.configuration import env
from uvicore.typing import OrderedDict

# This is the main wiki config.  All items here can be overridden
# when used inside other applications.  Accessible at config('mreschke.wiki')

config = {

    # --------------------------------------------------------------------------
    # Web Configuration
    #
    # prefix: All web routes will be prefixed with this URI. Ex: '' or '/wiki'
    #         This is in addition to running apps web.prefix config
    # --------------------------------------------------------------------------
    'web': {
        'prefix': '',
    },

    # --------------------------------------------------------------------------
    # Api Configuration
    #
    # prefix: All api routes will be prefixed with this URI. Ex: '' or '/wiki'
    #         This is in addition to running apps api.prefix config
    # --------------------------------------------------------------------------
    'api': {
        'prefix': '',
    },


    # --------------------------------------------------------------------------
    # Database Connections
    # --------------------------------------------------------------------------
    'database': {
        'default': 'wiki',
        'connections': {
            'wiki': {
                'driver': env('DB_WIKI_DRIVER', 'mysql'),
                'dialect': env('DB_WIKI_DIALECT', 'pymysql'),
                'host': env('DB_WIKI_HOST', '127.0.0.1'),
                'port': env.int('DB_WIKI_PORT', 3306),
                'database': env('DB_WIKI_DB', 'wiki'),
                'username': env('DB_WIKI_USER', 'root'),
                'password': env('DB_WIKI_PASSWORD', 'techie'),
                'prefix': env('DB_WIKI_PREFIX', None),
            },
        },
    },


    # --------------------------------------------------------------------------
    # Redis Connections
    # --------------------------------------------------------------------------
    'redis': {
        'default': env('REDIS_DEFAULT', 'wiki'),
        'connections': {
            'wiki': {
                'host': env('REDIS_WIKI_HOST', '127.0.0.1'),
                'port': env.int('REDIS_WIKI_PORT', 6379),
                'database': env.int('REDIS_WIKI_DB', 0),
                'password': env('REDIS_WIKI_PASSWORD', None),
            },
            'cache': {
                'host': env('REDIS_CACHE_HOST', '127.0.0.1'),
                'port': env.int('REDIS_CACHE_PORT', 6379),
                'database': env.int('REDIS_CACHE_DB', 2),
                'password': env('REDIS_CACHE_PASSWORD', None),
            },
        },
    },


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
    # requires them.  Services like uvicore.database, uvicore.orm, uvicore.auth
    # uvicore.http, etc...
    # --------------------------------------------------------------------------
    'dependencies': OrderedDict({
        # Wiki uses database, orm, auth, http
        'uvicore.foundation': {
            'provider': 'uvicore.foundation.services.Foundation',
        },
        'uvicore.redis': {
            'provider': 'uvicore.redis.services.Redis',
        },
        'uvicore.database': {
            'provider': 'uvicore.database.services.Database',
        },
        'uvicore.orm': {
            'provider': 'uvicore.orm.services.Orm',
        },
        'uvicore.auth': {
            'provider': 'uvicore.auth.services.Auth',
        },
        'uvicore.http': {
            'provider': 'uvicore.http.services.Http',
        },
        # 'mreschke.fusionauth': {
        #     'provider': 'mreschke.fusionauth.services.fusionauth.Fusionauth',
        # },
    }),

}
