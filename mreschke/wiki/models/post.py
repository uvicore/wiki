from __future__ import annotations
import uvicore
from typing import Optional
from uvicore.auth.models import User
from mreschke.wiki.models import Format
from uvicore.support.dumper import dd, dump
from mreschke.wiki.database.tables import posts as table
from uvicore.orm import BelongsTo, Field, Model, ModelMetaclass

@uvicore.model()
class Post(Model['Post'], metaclass=ModelMetaclass):
    """Wiki Posts"""

    # Database table definition
    __tableclass__ = table.Posts

    id: Optional[int] = Field('id',
        primary=True,
        description='Post ID',
        read_only=True,
    )

    slug: str = Field('slug',
        description='URL Friendly Post Title Slug',
        required=True,
    )

    title: str = Field('title',
        description='Post Title',
        required=True,
    )

    body: str = Field('body',
        description='Post Body',
    )

    format_key: str = Field('format_key',
        description='Post Format',
        required=True,
    )

    format: Optional[Format] = Field(None,
        description='Post Format',
        relation=BelongsTo('mreschke.wiki.models.format.Format', foreign_key='key', local_key='format_key'),
    )

    view_count: int = Field('view_count',
        description='Total Post Views',
    )

    deleted: bool = Field('deleted',
        description='Post is Deleted',
        default=False,
    )

    hidden: bool = Field('hidden',
        description='Post is Hidden',
        default=False,
    )

    # space_id: int = Field('space_id',
    #     description='Space ID',
    #     required=True,
    # )


    creator_id: int = Field('creator_id',
        description='Post Creator UserID',
        required=True,
    )

    # One-To-Many Inverse (One Post has One Creator)
    creator: Optional[User] = Field(None,
        description="Post Creator User Model",
        #relation=BelongsTo('uvicore.auth.models.user.User', 'id', 'creator_id'),
        relation=BelongsTo('uvicore.auth.models.user.User'),
    )

    updator_id: int = Field('updator_id',
        description='Post Updator UserID',
        required=True,
    )

    updator: Optional[User] = Field(None,
        description="Post Creator User Model",
        relation=BelongsTo('uvicore.auth.models.user.User'),
    )

    created_at: str = Field('created_at',
        description='Post Created DateTime',
    )

    updated_at: str = Field('updated_at',
        description='Post Updated DateTime',
    )

    indexed_at: str = Field('indexed_at',
        description='Post Last Indexed DateTime',
    )


# Import relation models at the bottom and update forward refs
#Post.update_forward_refs()
