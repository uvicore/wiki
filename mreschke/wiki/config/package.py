from collections import OrderedDict

# Package configuration is not meant to be overridden when used inside other
# apps.  This information is always unchanged and consistent.  The main
# wiki.py configuration however is meant to be overridden per use case.
# This is merged inside the main wiki.py and accessible at
# config('mreschke.wiki.package')
config = {

    # --------------------------------------------------------------------------
    # Package Information
    # --------------------------------------------------------------------------
    'name': 'mreschke.wiki',
    'config_prefix': 'mreschke.wiki',


    # --------------------------------------------------------------------------
    # Service Provider Dependencies
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
    'services': OrderedDict({
        # Uvicore Framework Service Providers
        'uvicore.foundation': {
            'provider': 'uvicore.foundation.services.Foundation',
        },
    }),

}
