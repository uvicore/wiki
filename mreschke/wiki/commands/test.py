#import typer
import json
import uvicore
from typing import List
from uvicore.console import command

#from uvicore import app, config
#from uvicore.db import SessionLocal, engine, Model
#from .. import models
#from fastapi import Depends
#from sqlalchemy.orm import Session
from uvicore.support.dumper import dump, dd

#from mreschke.wiki import db

# Commands
#cli = typer.Typer()

@command()
async def cli():
    #await misc()
    #await query_post_by_slug()
    await query_spaces()
    #await url_query()


async def url_query():

    where = """{
    "id": 1,
    "name": ["like", "some name"],
    "email": ["in", ["one", "two"]]
}"""

    dump('where=' + str(json.loads(where)))
    dump("DONE!")


async def query_post_by_slug():

    from mreschke.wiki.models import Post
    posts = await (Post.query()
        .include('topic.section.space')
        # /dev/apps/tools
        .where('topic.slug', '/tools')
        .where('topic.section.slug', '/apps')
        .where('topic.section.space.slug', '/dev')
        .get()
    )
    dump(posts)
    dump(len(posts))
    dump("DONE!")


async def query_spaces():
    from mreschke.wiki.models import Space
    spaces = await (Space.query()
        .include('sections', 'sections.topics')
        .where('sections.name', 'Production')
        .order_by('order')
        .sort(['sections.order', 'sections.topics.order'])
        .get()
    )
    dump(spaces)

    dump("DONE!")



async def misc():
    """Play asdfasdfasdfasdf"""


    # The reverse
    # from mreschke.wiki.models import SpaceSectionTopic
    # topics = await SpaceSectionTopic.query().include('section.space').get()
    # dd(topics)


    # from uvicore.auth.models import User
    # user = await (User.query()
    #     .where('disabled', '1')
    #     .include('groups')
    #     #.find(username='anonymous')
    #     .find(1)
    # )
    # dd(user)
    # #['roles', 'roles.permissions', 'groups', 'groups.roles', 'groups.roles.permissions']


    dd('DONE')


    from uvicore.typing import Dict, OrderedDict, Optional


    # from dataclasses import dataclass
    # @dataclass
    # class Config:
    #     name: Optional[str] = None
    #     registers: Optional[Dict] = None


    # x = Config()
    # x.name = 'matthew'
    # x.registers = {
    #     'models': True
    # }
    # x.asdf = 'hi'
    # x.name = 1
    # dump(x.asdf)
    # dd(x)


    dump(uvicore.config)
    #dump(uvicore.config('mreschke.wiki.database'))

    dd('DONE')

    #dd(uvicore.config)

    #dd(uvicore.app.packages.mreschke.wiki)
    #dd(uvicore.app.package('mreschke.wiki').name)


    a = Dict({
        'name': 'Mreschke Wiki',
        'registers': {
            'modules': True,
            'tables': True,
        },
        'database': {
            'default': 'wiki',
            'connections': {
                'wiki': {
                    'server': 'localhost',
                    'port': 3308
                }
            }
        }
    })


    b = {
        'name': 'NEW name',
        'database': {
            'connections': {
                'wiki': {
                    'port': 99999
                }
            }
        }
    }

    a.merge(b)


    #a.dotset('database.connections.wiki.asdf.asdf.asdf', 1234)

    #dump(a.dotget('database.connections.wiki.port'))

    dump(a.dotget('database.connections.wiki.port'))


    dd(a)
    dd('done')
    #dd(a)

    # a.defaults(b)

    # a.freeze()

    # a.unfreeze()
    # a.asdfasdfasdf = 'asdfasdf'

    # dd(a)




    #x = config('app.name')


    x = config.app.name



    config('app.name', 'newname')
    config.app.name = 'newname'











    x = Config(name='matthew', registers={'modules': True})
    dd(x)



    dump(config['name'])
    dump(config.name)
    if 'name' in config:
        dump('name found')

    if config.name:
        dump('name found again')

    if config.asdfasdfasdfasdfasdf:
        dump('asdfasdfasdfasdfasdfasdfasdfasdf')

    dump(config.database.connections.wiki)

    if config.database.connections:
        dump('connections found')



    # Add something DEEP without defining parents
    config.frameworks.laravel.color = ['red', 'blue']




    dump(config)







    dd('DONE PLAYING')
























































    from mreschke.wiki.models.post import Post

    posts = (await Post.query()
        .include('creator')
        .get()
    )
    dump(posts)


    # from uvicore.support import module
    # x = module.location('uvicore.auth.database')
    # #x = module.location('uvicore.foundation.config.package.config')

    # dd(x)


    # await db_play()
    # #encode_play()
    # # dd('Done Playing!')



    # """Wiki Test command"""

    # uvicore.config.merge('mreschke.wiki.database', {'test': 'hi'})
    # dd(uvicore.config('mreschke.wiki'))



    # # Manuall get app singleton
    # from uvicore.contracts import Application
    # app: Application = uvicore.ioc.make('app')
    # dump(app.config('app.name'))

    # dump('x')

    # # Can manually get config too
    # config = uvicore.ioc.make('config')
    # dump(config('app.name'))

    # # Log example
    # uvicore.log.header('hi')

    # # Pull log from IoC
    # log = uvicore.ioc.make('Logger')

    # log.header('there')
    # #dd(uvicore.ioc.bindings)


    # # module = 'uvicore'
    # # parts = module.split('.')
    # # path = '.'.join(parts[0:-1])
    # # name = ''.join(parts[-1:])

    # # if path == '': path = module
    # # imported = import_module(path)
    # # dd(getattr(imported, name))

    # wiki = app.package('mreschke.wiki')
    # dump(wiki.config())


    # log('hi')

    # dd('test done')



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



async def db_play():

    from uvicore import db
    from mreschke.wiki.models.post import Post
    from uvicore.auth.models.user import User

    # dump(db.default)
    # dump(db.connections)
    # dump(db.engines)

    # True Raw, matching SQLA Core
    # engine = db.engine('wiki')
    # con = engine.connect()
    # table = User.__table__
    # query = table.select()
    # users = con.execute(query)
    # for user in users:
    #    dump(user)
    #    dump(user['name'])
    #    dump(user.name)
    # dd(users)


    # Not so raw, no engine, no connection, using User entity
    # query = User.__table__.select()
    # users = db.execute(User, query)
    # for user in users:
    #     dump(user)
    #     dump(user['name'])
    #     dump(user.name)
    # dd(users)

    # Model usage
    #dd(db.metadata.get('wiki').tables)
    #dd(User.__fields__['id'].field_info.extra['sortable'])
    #dd(User.info(True))

    #dd(Post.find(1))

    #x: Post = Post.find(1)
    #dd(x)

    from asgiref.sync import async_to_sync
    from time import sleep

    #engine = db.engine('wiki')
    #async_to_sync(engine.connect)()
    #engine.connect()

    #dd(Post.info())

    posts: List[Post] = await Post.all()

    #posts = Post.include('creator').get()
    #for post in posts:
        #dd(post.creator)
    dump(posts)

    #users: List[User] = User.get()
    #users = User.where('id', 1).get()

    #dump(users)

    #exit()



    #users = User.where('id', '1').get()
    # for user in users:
    #     dd(user.hi())
    #dd(users)

    # user = User.find(1)
    # dd(user)





    # table = User.Db.table
    # query = table.select()
    # users = db.fetchall(User, query)
    # for user in users:
    #     dump(user)
    #     dump(user['name'])
    #     dump(user.name)

    # dump('--------------')
    # query = table.select().where(table.c.id == 1)
    # user = db.fetchone(User, query)
    # dump(user)
    # dump(user.name)


    # #dd(User.all())

    # #x = db().table('users').get()
    # users = db().table('users').get()
    # for user in users:
    #     dd(user['name'])
    # dd(x)
    # dd(x._connection, x._table, x._where)


    # dump(uvicore.ioc.make('db')())
    # dump(uvicore.ioc.make('db')())
    # dump(db())
    # dump(db())
    # dump(db())
    #x = db.connection('wiki').table('users').get()
    #dump(x)

    #dd('x')


    # DB::connection('foo')->select(...)
    # $users = DB::select('select * from users where active = ?', [1]);
    # DB::select('select * from users where id = :id', ['id' => 1]);

    # DB::transaction(function () {
    #     DB::table('users')->update(['votes' => 1]);

    #     DB::table('posts')->delete();
    # });

    # $users = DB::table('users')->get();
    # DB::table('users')->where('name', 'John')->first();
    # DB::table('users')->where('name', 'John')->value('email');
    # DB::table('users')->find(3);
    # DB::table('roles')->pluck('title', 'name');
    # DB::table('users')->count();
    # DB::table('orders')->max('price');
    #$users = DB::table('users')->select('name', 'email as user_email')->get();
    #$users = DB::table('users')->distinct()->get();
    #$users = $query->addSelect('age')->get();

    # $users = DB::table('users')
    #     ->join('contacts', 'users.id', '=', 'contacts.user_id')
    #     ->join('orders', 'users.id', '=', 'orders.user_id')
    #     ->select('users.*', 'contacts.phone', 'orders.price')
    #     ->get();

    #dd('hi')


def encode_play():

    # None of this works because all encode uses await, and you cannot call
    # any await method unless every def is async def
    # So we do have to split our database query build + ORM into both sync
    # and async

    from uvicore import db
    import sqlalchemy as sa
    from databases import Database

    connection = 'wiki'

    database = Database('mysql://root:techie@127.0.0.1:3306/uvicore_wiki')
    database.connect()

    table = sa.Table(
        "users",
        db.metadata.get(connection),
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=50))
    )

    #engine = db.engine('wiki')
    #con = db.connect()
    query = table.select()
    users = database.fetch_all(query)
    # for user in users:


    # table = User.Db.table
    # query = table.select()
    # users = con.execute(query)


    dd('DONE encode_play()')
