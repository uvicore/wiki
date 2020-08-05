import typer
import uvicore
#from uvicore import app, config
#from uvicore.db import SessionLocal, engine, Model
#from .. import models
#from fastapi import Depends
#from sqlalchemy.orm import Session
from uvicore.support.dumper import dump, dd

#from mreschke.wiki import db

# Commands
cli = typer.Typer()


@cli.command()
def test():
    """Wiki Test command"""

    uvicore.config.merge('mreschke.wiki.database', {'test': 'hi'})
    dd(uvicore.config('mreschke.wiki'))



    # Manuall get app singleton
    from uvicore.contracts import Application
    app: Application = uvicore.ioc.make('app')
    dump(app.config('app.name'))

    dump('x')

    # Can manually get config too
    config = uvicore.ioc.make('config')
    dump(config('app.name'))

    # Log example
    uvicore.log.header('hi')

    # Pull log from IoC
    log = uvicore.ioc.make('Logger')

    log.header('there')
    #dd(uvicore.ioc.bindings)


    # module = 'uvicore'
    # parts = module.split('.')
    # path = '.'.join(parts[0:-1])
    # name = ''.join(parts[-1:])

    # if path == '': path = module
    # imported = import_module(path)
    # dd(getattr(imported, name))

    wiki = app.package('mreschke.wiki')
    dump(wiki.config())


    log('hi')

    dd('test done')



    # from mreschke.wiki.models.user import User
    # user = User.find(1)
    # print(user)
    # print(user.name)

    # print('----')

    # users = User.all()
    # print(users)
    # for user in users:
    #     print(user.hi())

    # print('----')

    # print(User)
    #db: Session = Depends(get_db)

    #db = get_db()
    #models.Base.metadata.create_all(bind=engine)
    #Model.metadata.create_all(bind=engine)

    # users = models.User.query.all()
    # for user in users:
    #     print(user.name)

    #print('hi')

    #db.create_all()

    #db = SessionLocal()
    #db.create_all()
    #users = db.query(User).all()
    #print(users)



    # print('wiki command')
    # print(config('wiki.key1'))
    # print(config('wiki'))

    # config.set('wiki.key1', {
    #     'kv1': 'test one',
    # })
    # config.set('wiki.key1.kv1', 'xxx')
    # print(config('wiki.key1'))
    # print(config('wiki'))
    # print(config())

    # config.set('wiki.test.one', 'asdfasdf')
    # print(config.get('wiki.test.one'))
    # print(config.get())

    # print(id(config))
