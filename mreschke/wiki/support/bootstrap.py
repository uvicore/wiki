import uvicore
from uvicore.configuration import Env
from uvicore.support import path
from uvicore.contracts import Application as ApplicationInterface
from uvicore.support.dumper import dd, dump

def application(is_console: bool = False) -> ApplicationInterface:
    """Bootstrap the application either from the CLI or Web entry points
    """

    # Base path
    base_path = path.find_base(__file__)

    # Load .env from environs
    Env().read_env(base_path + '/.env')

    # Import this apps config (import must be after Env())
    from ..config.app import config as app_config

    # Bind bootstrap level IoC overrides
    uvicore.ioc.bind_map(app_config['ioc'])

    # Example of manual bootstrap level custom IoC bindings
    #from uvicore.foundation.application import Application
    # uvicore.ioc.bind(
    #     name='Application',
    #     object='uvicore.foundation.application._Application',
    #     #kwargs={'test': 'hixx'},
    #     singleton=True,
    #     aliases=['App']
    # )

    # Exampel if making an object with a factory
    # uvicore.ioc.bind(
    #     name='Logger',
    #     object='uvicore.support.logger._Logger',
    #     #factory='uvicore.factory.logger.Logger',
    #     # If factory, kwargs are for factory
    #     kwargs={'config': app_config['logger']},
    #     singleton=True,
    #     aliases=['Log', 'log', 'logger']
    # )



    # Instantiate the Application into the uvicore.app instance
    uvicore.app = uvicore.ioc.make('Application')
    #dd(uvicore.app)

    # Bootstrap the Uvicore Application (Either CLI or HTTP entry points based on is_console)
    uvicore.app.bootstrap(app_config, base_path, is_console)

    wiki = uvicore.app.package('mreschke.wiki')
    dd(wiki.config('route'))
    dd('hi')

    # If you wanted to get the instance of the app without import
    # just make it from its IoC singleton
    # from uvicore.contracts import Application
    # app2: Application = uvicore.ioc.make('App')
    # dump(app2.providers)


    #dump(app.providers)
    #dump(app.packages)


    #dd(Application.packages)
    #dd(uvicore.app.packages)



    #foundation = app.package('foundation')
    #foundation = app.package(module='uvicore.foundation')
    #dump(foundation)
    #dump(foundation.config())

    #dump(app.config())

    #wiki = uvicore.app.package('wiki')
    #dd(wiki.config('route'))
    #dump(wiki.config())

    #dump(app.config('wiki'))

    #main = app.package(main=True)
    #dump(main)

    #dd('x')

    # Return application
    return uvicore.app























# #from uvicore import app
# from uvicore.support.helpers import find_base_path
# from uvicore.support.dumper import dd, dump
# from environs import Env

# def application(is_console: bool = False):
#     """Bootstrap the application either from the CLI or Web entrypoints
#     """

#     import uvicore

#     from uvicore.support.config import Config
#     uvicore.config = Config()

#     from uvicore.foundation.application import Application
#     from uvicore import Package
#     uvicore.app = Application(uvicore.config, Package)




#     # Base path
#     path = find_base_path(__file__)

#     # Load .env from environs
#     Env().read_env(path + '/.env')

#     # Import this apps config (import must be after Env())
#     from ..config.app import app as app_config

#     # Bootstrap the Uvicore Application (Either CLI or HTTP entrypoints)
#     uvicore.app.bootstrap(app_config, path, is_console)


#     #dump(app.providers)
#     #dump(app.packages)

#     #foundation = app.package('foundation')
#     #foundation = app.package(module='uvicore.foundation')
#     #dump(foundation)
#     #dump(foundation.config())

#     #dump(app.config())

#     #wiki = uvicore.app.package('wiki')
#     #dd(wiki)
#     #dump(wiki.config())

#     #dump(app.config('wiki'))

#     #main = app.package(main=True)
#     #dump(main)

#     #dd('x')

#     # Return application
#     return uvicore.app
