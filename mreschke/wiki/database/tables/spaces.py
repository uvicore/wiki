import uvicore
import sqlalchemy as sa
from uvicore.database import Table
from uvicore.support.dumper import dump, dd

# Get related tablenames with proper prefixes
users = uvicore.db.tablename('auth.users')
formats = uvicore.db.tablename('wiki.formats')


@uvicore.table()
class Spaces(Table):

    # Actual database table name
    # Plural table names and singluar model names are encouraged
    # Do not add a package prefix, leave that to the connection config
    name = 'spaces'

    # Connection for this database from your config file
    connection = 'wiki'

    # SQLAlchemy Table definition as a list (exclude name and metadata)
    # This will be converted into an actual SQLAlchemy Table() instance
    # See https://docs.sqlalchemy.org/en/13/core/schema.html
    schema = [
        # Defaults: nullable=False, index=False, unique=False, primary_key=False

        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('slug', sa.String(length=50), unique=True),
        sa.Column('section', sa.String(length=50)),
        sa.Column('name', sa.String(length=50)),
        sa.Column('order', sa.SmallInteger),
    ]

    # Optional SQLAlchemy Table() instance kwargs
    schema_kwargs = {}
