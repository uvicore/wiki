# This is the main wiki config.  All items here can be overridden
# when used inside other applications.  Accessible at config('mreschke.wiki')

config = {

    # --------------------------------------------------------------------------
    # Registration Control
    # --------------------------------------------------------------------------
    # This lets you control the service provider registrations.  If this app
    # is used as a package inside another app you might not want some things
    # registered in that context.
    'registers': {
        'web_routes': True,
        'api_routes': True,
        'middleware': True,
        'views': True,
        'assets': True,
        'commands': True,
        'models': True,
        'tables': True,
        'seeders': True,
    },


    # --------------------------------------------------------------------------
    # Route Configuration
    # --------------------------------------------------------------------------
    # Or like so, no underscores, so in dot notation config('blog.route.prefix')
    # have to do deep merges
    'route': {
        'web_prefix': '/wiki',
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


    # --------------------------------------------------------------------------
    # Database Connections
    # --------------------------------------------------------------------------
    'database': {
        'default': 'wiki',
        'connections': {
            'wiki': {
                'driver': 'mysql',
                'dialect': 'pymysql',
                'host': '127.0.0.1',
                'port': 3306,
                'database': 'uvicore_wiki',
                'username': 'root',
                'password': 'techie',
                'prefix': None,
                #'include_connections': ['auth']
            },
            # 'some-sql': {
            #     'driver': 'mysql',
            #     'dialect': 'pymysql',
            #     'host': '127.0.0.1',
            #     'port': 3306,
            #     'database': 'somesql',
            #     'username': 'root',
            #     'password': 'techie',
            #     'prefix': None,
            # },
        },
    },

    # Bundle?  Canot use package, that is pythonic, all apps/libs ARE packages



    #include API also, yes/no, maybe that goes with register_routes


    # What all can be overwritten when in library mode?
    # database
    # route prefix
    # caching location
    # which parts are used (views, routes, or just cli and code)


}
