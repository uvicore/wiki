from __future__ import annotations
import uvicore
from typing import Optional
from uvicore.auth.models import User
from mreschke.wiki.models.format import Format
from uvicore.support.dumper import dd, dump
from mreschke.wiki.database.tables import posts as table
from uvicore.orm import BelongsTo, Field, Model, ModelMetaclass
from datetime import datetime
from mreschke.wiki.models.topic import Topic

import markdown

def to_markdown(row):
    config = {
        'extra': {
            'footnotes': {
                'UNIQUE_IDS': True
            },
            'fenced_code': {
                'lang_prefix': 'lang-'
            }
        },
        'toc': {
            'permalink': True
        }
    }
    return markdown.markdown(row['body'],
        extensions=[
            'extra',
            'toc',
            'sane_lists',
            'nl2br',
            'wikilinks',
        ],
        extension_configs=config,
    )


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
        evaluate=to_markdown
    )

    format_key: str = Field('format_key',
        description='Post Format Key',
        required=True,
    )

    format: Optional[Format] = Field(None,
        description='Post Format Model',
        read_only=True,
        relation=BelongsTo('mreschke.wiki.models.Format', foreign_key='key', local_key='format_key'),
    )

    topic_id: int = Field('topic_id',
        description='Post Topic ID',
        required=True,
    )

    topic: Optional[Topic] = Field(None,
        description='Post Topic Model',
        relation=BelongsTo('mreschke.wiki.models.Topic')
    )

    view_count: int = Field('view_count',
        description='Total Post Views',
        default=0,
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
        read_only=True,
        #relation=BelongsTo('uvicore.auth.models.user.User', 'id', 'creator_id'),
        relation=BelongsTo('uvicore.auth.models.User'),
    )

    updator_id: int = Field('updator_id',
        description='Post Updator UserID',
        required=True,
    )

    updator: Optional[User] = Field(None,
        description="Post Creator User Model",
        read_only=True,
        relation=BelongsTo('uvicore.auth.models.User'),
    )

    created_at: datetime = Field('created_at',
        description='Post Created DateTime',
        read_only=True,
    )

    updated_at: datetime = Field('updated_at',
        description='Post Updated DateTime',
        read_only=True,
    )

    indexed_at: Optional[datetime] = Field('indexed_at',
        description='Post Last Indexed DateTime',
        #read_only=True,
    )



# Import relation models at the bottom and update forward refs
#Post.update_forward_refs()
