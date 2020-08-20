config = {
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
