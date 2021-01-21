import uvicore
import sqlalchemy as sa
from uvicore.database import Table
from uvicore.support.dumper import dump, dd

# Get related tablenames with proper prefixes
users = uvicore.db.tablename('auth.users')
formats = uvicore.db.tablename('wiki.formats')


@uvicore.table()
class Formats(Table):

    # Actual database table name
    # Plural table names and singluar model names are encouraged
    # Do not add a package prefix, leave that to the connection config
    name = 'formats'

    # Connection for this database from your config file
    connection = 'wiki'

    # SQLAlchemy Table definition as a list (exclude name and metadata)
    # This will be converted into an actual SQLAlchemy Table() instance
    # See https://docs.sqlalchemy.org/en/13/core/schema.html
    schema = [
        # Defaults: nullable=False, index=False, unique=False, primary_key=False
        sa.Column('key', sa.String(length=3), primary_key=True),
        sa.Column('name', sa.String(length=20)),
    ]

    # Optional SQLAlchemy Table() instance kwargs
    schema_kwargs = {}
