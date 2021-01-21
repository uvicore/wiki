import uvicore
import sqlalchemy as sa
from uvicore.database import Table
from uvicore.support.dumper import dump, dd

# Get related tablenames with proper prefixes
users = uvicore.db.tablename('auth.users')
formats = uvicore.db.tablename('wiki.formats')


@uvicore.table()
class Posts(Table):

    # Actual database table name
    # Plural table names and singluar model names are encouraged
    # Do not add a package prefix, leave that to the connection config
    name = 'posts'

    # Connection for this database from your config file
    connection = 'wiki'

    # SQLAlchemy Table definition as a list (exclude name and metadata)
    # This will be converted into an actual SQLAlchemy Table() instance
    # See https://docs.sqlalchemy.org/en/13/core/schema.html
    schema = [
        # Defaults
        #   nullable = False

        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('slug', sa.String(length=100), unique=True),
        sa.Column('title', sa.String(length=100)),
        sa.Column('body', sa.Text()),
        sa.Column('format_key', sa.String(length=3), sa.ForeignKey(f"{formats}.key"), nullable=False),
        sa.Column('view_count', sa.Integer),
        sa.Column('deleted', sa.Boolean(), default=False),
        sa.Column('hidden', sa.Boolean(), default=False),
        sa.Column('creator_id', sa.Integer, sa.ForeignKey(f"{users}.id"), nullable=False),
        sa.Column('updator_id', sa.Integer, sa.ForeignKey(f"{users}.id"), nullable=False),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime()),
        sa.Column('indexed_at', sa.DateTime()),
    ]

    # Optional SQLAlchemy Table() instance kwargs
    schema_kwargs = {}


# IoC Class Instance
#Posts: _Posts = uvicore.ioc.make('mreschke.wiki.database.tables.posts.Posts', _Posts, singleton=True)




# # Actual database table name
# # Usually tabkes are plural while models are signular
# tablename = 'posts'

# # Connection for this database from your config file
# connection = 'wiki'

# # SQLAlchemy connection metedata this table belongs to
# metadata = db.metadata.get(connection)

# # Table object details
# table = Table(tablename, connection,
#     # Actual SQLAlchemy Table definition
#     # See https://docs.sqlalchemy.org/en/13/core/schema.html
#     schema=sa.Table(tablename, metadata,
#         sa.Column("id", sa.Integer, primary_key=True),
#         sa.Column("slug", sa.String(length=100), unique=True),
#         sa.Column("title", sa.String(length=100)),

#         # Automatically add owner_id, creator_id, updator_id,
#         # created_at, updated_at columns required for Uvicore auth and logging
#         #*autocolumns
#     ),
# )


# table = Table('posts', 'wiki',
#     # Actual SQLAlchemy Table definition
#     # See https://docs.sqlalchemy.org/en/13/core/schema.html
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column("slug", sa.String(length=100), unique=True),
#     sa.Column("title", sa.String(length=100)),

#     # Automatically add owner_id, creator_id, updator_id,
#     # created_at, updated_at columns required for Uvicore auth and logging
#     #*autocolumns
# )
