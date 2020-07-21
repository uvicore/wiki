# Entire blog config is meant to be overwritten when
# you include it as a library.  For example in a CMS
# you might change the route_prefix to /blog instead of /

config = {
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
            },
            'some-sql': {
                'driver': 'mysql',
                'dialect': 'pymysql',
                'host': '127.0.0.1',
                'port': 3306,
                'database': 'somesql',
                'username': 'root',
                'password': 'techie',
                'prefix': None,
            },

        },
    },

    # Bundle?  Canot use package, that is pythonic, all apps/libs ARE packages


    # These let you control the service provider
    # Maybe you want the library part but want NO web part, no routes, no views
    'register_web_routes': True,
    'register_api_routes': True,
    'register_views': True,
    'register_assets': True,
    'register_commands': True,
    # ??register_configs??

    #include API also, yes/no, maybe that goes with register_routes


    # What all can be overwritten when in library mode?
    # database
    # route prefix
    # caching location
    # which parts are used (views, routes, or just cli and code)




    'key1': 'blog.key1 config here',
}
