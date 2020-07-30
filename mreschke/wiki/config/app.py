from collections import OrderedDict
from uvicore.configuration import env


config = {

    # --------------------------------------------------------------------------
    # App Information
    # --------------------------------------------------------------------------
    'name': 'My Wiki',
    'main': 'mreschke.wiki',
    'debug': False,


    # --------------------------------------------------------------------------
    # Uvicorn Development Server
    # --------------------------------------------------------------------------
    # This configures the dev server when you run `./uvicore http serve`
    'server': {
        'app': 'mreschke.wiki.http.server:http',
        'host': env('SERVER_HOST', '127.0.0.1'),
        'port': env.int('SERVER_PORT', 5000),
        'reload': env.bool('SERVER_RELOAD', True),
        'access_log': env.bool('SERVER_ACCESS_LOG', True),
    },


    # --------------------------------------------------------------------------
    # OpenAPI Auto API Doc Configuration
    # --------------------------------------------------------------------------
    'openapi': {
        'title': 'Wiki API Docs',
        'url': '/openapi.json',
        'docs_url': '/docs',
        'redoc_url': '/redoc',
    },

    # --------------------------------------------------------------------------
    # Package Dependencies (Service Providers)
    # --------------------------------------------------------------------------
    # Packages add functionality to your applications.  In fact your app itself
    # is a package that can be used inside any other app.  Uvicore framework is
    # also split into packages which use services providers to inject core
    # functionality.  Order matters for override/deep merge purposes.  Each
    # package overrides items of the previous, so the last package wins.
    # Example, configs defined with the same key are deep merged with last
    # one winning. Defining your actual apps package last means it will win
    # in all override battles.
    # Overrides include: providers, configs, views, templates, assets
    'packages': OrderedDict({
        # # Uvicore Framework Service Providers
        # 'uvicore.foundation': {
        #     # Foundation itself is a package which relies on many other services
        #     # like configuration, logging...all of which you can override.
        #     'provider': 'uvicore.foundation.services.Foundation',
        #     #'config': 'uvicore.logging.config.app.config',
        # },

        # EXAMPLE.  You can override any service provider by simply providing
        # your own provider with the same key.  To override the logger you have
        # two options.  Either override the entire service provider with your
        # own like this.  Or use the 'bindings' array below to override just the
        # class that is used in the original uvicore logging service provider.
        # 'uvicore.logging': {
        #     'provider': 'mreschke.wiki.services.logging.Logging',
        # },

        # Application Service Providers
        'mreschke.wiki': {
            'provider': 'mreschke.wiki.services.wiki.Wiki',
        },
    }),


    # --------------------------------------------------------------------------
    # Service Provider Binding Definitions
    # --------------------------------------------------------------------------
    # Most service providers bind classes into the IoC.  Most uvicore framework
    # providers will lookup this array to let you override which classes they
    # actually bind into the container.  This lets you quickly override an
    # existing service provider binding without actually using the 'services'
    # array above to define your own complete service provider.  Often times
    # simply overriding the bound class is good enough.
    'bindings': {
        'Logger': 'mreschke.wiki.services.framework.logger.Logger',
        'Configuration': 'mreschke.wiki.services.framework.configuration.Configuration',
    },


    # --------------------------------------------------------------------------
    # Inversion of Control (IoC) Concrete Implimentation Overrides
    # --------------------------------------------------------------------------
    # Many core or small classes do not use service providers at all.  But all
    # classes use the IoC for their implimentation to allow you to override
    # anything, even the smallest of classes.  Use this section to override all
    # other non service provider based classes.  If the array is empty the
    # defaults in `uvicore/container/ioc.py` are used.
    'ioc': {
        'Application': {
            'object': 'mreschke.wiki.services.framework.application.Application',
            'singleton': True,
            'aliases': ['App']
        },
        'Package': {
            #'object': 'uvicore.foundation.package._Package',
            'object': 'mreschke.wiki.services.framework.package.Package',
            'aliases': ['package']
        },
    },


    # --------------------------------------------------------------------------
    # Logging Configuration
    # --------------------------------------------------------------------------
    # The uvicore.logger packages does NOT provide its own config
    # because it needs to load super early in the bootstrap process.
    # So we define the logger config right here instead.  Tweak as needed.
    'logger': {
        'console': {
            'enabled': env.bool('LOG_CONSOLE_ENABLED', True),
            'level': env('LOG_CONSOLE_LEVEL', 'WARNING'),
            'colors': env.bool('LOG_CONSOLE_COLORS', True),
        },
        'file': {
            'enabled': env.bool('LOG_FILE_ENABLED', True),
            'level': env('LOG_FILE_LEVEL', 'WARNING'),
            #'file': config.LOG_PATH + '/' + date.today().strftime('%Y-%m-%d') + '_permits.log',
            'file': '/tmp/uvicore.log',
        }
    },


    # Add more laravel stuff, locale, timezone etc...

}
