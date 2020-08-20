import sqlalchemy as sa
from uvicore import db
from uvicore.database.table import Table, autocolumns
from uvicore.support.dumper import dump, dd

class Posts(Table):

    tablename = 'posts'
    connection = 'wiki'
    metadata = db.metadata.get(connection)

    schema = sa.Table(tablename, metedata,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("slug", sa.String(length=100), unique=True),
        sa.Column("title", sa.String(length=100)),
    )







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
