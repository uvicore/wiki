import typer
from uvicore import app, config
#from uvicore.db import SessionLocal, engine, Model
#from .. import models
#from fastapi import Depends
#from sqlalchemy.orm import Session

#from mreschke.wiki import db


cli = typer.Typer()

@cli.command()
def test():
    """Wiki Test command"""

    from mreschke.wiki.models.user import User
    user = User.find(1)
    print(user)
    print(user.name)

    print('----')

    users = User.all()
    print(users)
    for user in users:
        print(user.hi())

    print('----')

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
