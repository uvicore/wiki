import typer
from  pydantic import BaseSettings, BaseModel
from pydantic import Field
from typing import Optional
from types import SimpleNamespace as obj
from collections import namedtuple
from typing import NamedTuple


cli = typer.Typer()

@cli.command()
def pydantic_config():

    class Settings(BaseSettings):
        class Config:
            env_file = base_path + '/.env'


    class Package(Settings):
        module: str
        provider: str


    class App(Settings):
        # App Info
        name: str = 'wiki'
        vendor: str = 'mreschke'
        module: str = 'mreschke.wiki'
        debug: bool = True

        # Uvicorn Dev Server
        class Server(Settings):
            class Config: env_prefix = 'server_'
            app: str = 'mreschke.wiki.http.server:app.http'
            host: str = '127.0.0.1'
            port: int = 5000
            reload: bool = True
            access_log: bool = True
        server = Server(port=333)

        # server = Server(
        #     app='mreschke.wiki.http.server:app.http',
        #     host='127.0.0.1',
        #     port=5000,
        #     reload=True,
        #     access_log=True
        # )
        # server.Config.env_prefix = 'server_'
        # server = Server()
        # server.app = 'mreschke.wiki.http.server:app.http'
        # server.host = '127.0.0.1'
        # server.port = 5000
        # server.reload = True
        # server.access_log = True
        # server.Config.env_prefix = 'server_'


        # Package Dependencies
        packages = [
            Package(module='moda', provider='prova')
        ]

    app_config = App()

    #config = namedtuple('Config2', ['app'])
    #config.app = app_config

    # config = obj(**{
    #     'app': app_config
    # })

    class Conf(NamedTuple):
        app: App

    #Conf.app = app_config

    config = Conf(app=app_config)


    dump(config.app.server)
    dump(app_config.server.host)
    dump(app_config.server.app)
    dump(app_config.packages[0].module)
    dd(app_config.dict())

    dd(App().dict())

