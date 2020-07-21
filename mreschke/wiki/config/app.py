from uvicore.configuration import env

# App and providers DO run if APP or LIBRARY mode
# Because even if module, it is a dependency graph
# So provider IMPORTER needs to not import things twice

# Providers should be a recursive dependency graph

# App config is only for when this app is RUNNING as a server
# It is not meant to be overwritten when its included as a LIBRARY

app = {
    # Package Info
    'name': 'wiki',
    'vendor': 'mreschke',
    'module': 'mreschke.wiki',
    'config_prefix': 'mreschke.wiki',
    'debug': False,

    # OpenAPI
    'openapi': {
        'title': 'Wiki API Docs',
        'url': '/openapi.json',
        'docs_url': '/docs',
        'redoc_url': '/redoc',
    },

    # Uvicorn Dev Server (./uvicore http serve)
    'server': {
        'app': 'mreschke.wiki.http.server:http',
        'host': env('SERVER_HOST', '127.0.0.1'),
        'port': env.int('SERVER_PORT', 5000),
        'reload': env.bool('SERVER_RELOAD', True),
        'access_log': env.bool('SERVER_ACCESS_LOG', True),
    },

    # Inversion of Control (IoC) Concrete Implimentation Overrides
    # See uvicore/foundation/ioc.py for a list of all possible mappings
    'ioc': {
        'Application': {
            'object': 'uvicore.foundation.application._Application',
            'singleton': True,
            'aliases': ['App']
        }
    },

    # Package paths (allows you to re-organize your app file structure)
    # So far NONE are used, because the service provide handles most explicitly
    # And do I really care?  It is an opinionated framework after all
    #'paths': {
        #'server': 'mreschke.wiki.http.server.http',
        #'controllers': 'mreschke.wiki.http.controllers',
        #'public': 'mreschke.wiki.http.public',
        #'views': 'mreschke.wiki.http.views',
        #'commands': 'mreschke.wiki.commands',
    #},

    # Add more laravel stuff, locale, timezone etc...

    # Dependent Package Service Providers
    # Order matters for override/deep merge purposes
    # Each provider overrides items of the previous, so the last provider wins
    # Example, configs defined with the same key are deep merged with last one winning
    # So define this actual app LAST to override all

    # Overrides - We want last one to win on everything
    # For configs, last one wins
    # For jinja view folders, last one wins ?? double check
    # For jinja globals, last one wins ?? double check
    'providers': [
        ('uvicore.foundation', 'providers.Foundation'),
        #('mrcore.auth', 'providers.AuthServiceProvider'),
        #('mrcore.cache', 'providers.CacheServiceProvider'),

        # Application (must be last to win in overrides)
        ('mreschke.wiki', 'providers.Wiki'),
    ],

    # Package Dependencies (JUST PLAYING)
    'packages': [
        {
            #'name': 'foundation',
            'module': 'uvicore.foundation',
            'provider': 'uvicore.foundation.providers.Foundation'
        },
        {
            #'name': 'wiki',
            'module': 'mreschke.wiki',
            'provider': 'mreschke.wiki.providers.Wiki',
        },
    ],

    'experimental_providers_like_mrcore_modules': {
        'mreschke.blog': {
            'console_only': True
            # cant think of anything else, like dynaron/theme
            # all those configs shouldn't live here, but in theme.py config itself
        }
    }

}
