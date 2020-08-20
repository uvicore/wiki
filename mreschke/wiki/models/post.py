import uvicore
from typing import Optional
from uvicore.orm.model import Model
from uvicore.orm.field import Field
from mreschke.wiki.database.tables.posts import Posts
from uvicore.support.dumper import dd, dump
import sqlalchemy as sa
from uvicore import db


class Post(Model):
    """Description, this shows up in openapi schemas section"""

    # Database connection and table information
    #__connection__ = posts.table.connection
    #__tablename__ = posts.table.name
    #__table__ = posts.table.schema
    __tableclass__ = Posts

    id: Optional[int] = Field('id',
        description='Post ID',
        sortable=True,
        searchable=True,
    )

    slug: str = Field('slug',
        description='URL Friendly Post Title Slug',
        required=True,
    )

    title: str = Field('title',
        description='Post Title',
        required=True,
    )
