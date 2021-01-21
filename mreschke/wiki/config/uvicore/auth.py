config = {

    # --------------------------------------------------------------------------
    # Registration Control
    # --------------------------------------------------------------------------
    # This lets you control the service provider registrations.  If this app
    # is used as a package inside another app you might not want some things
    # registered in that context.
    'registers': {
        # 'web_routes': False,
        # 'api_routes': False,
        # 'middleware': False,
        # 'views': False,
        # 'assets': False,
        # 'commands': True,

        # Database
        #'models': False,
        #'tables': False,
        #'seeders': False,
    },


    # --------------------------------------------------------------------------
    # Database Connections
    # --------------------------------------------------------------------------
    'database': {
        'default': 'auth',
        'connections': {
            'auth': {
                'driver': 'mysql',
                'dialect': 'pymysql',
                'host': '127.0.0.1',
                'port': 3306,
                'database': 'uvicore_wiki',
                'username': 'root',
                'password': 'techie',
                'prefix': 'auth_',
            },
        },
    },
}
