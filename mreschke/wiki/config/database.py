# Example of splitting out configs into multiple files
# All done in the wikis service provider

config = {

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

}
