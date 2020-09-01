from typing import Optional
from uvicore.orm.model import Model
from uvicore.orm.fields import Field
from mreschke.wiki.database.tables import posts
from uvicore.support.dumper import dd, dump

from uvicore.auth.models.user import User


class Post(Model):
    """Wiki Posts"""

    # Database table definition
    __tableclass__ = posts.Table

    id: Optional[int] = Field('id',
        description='Post ID',
        sortable=True,
        searchable=True,
    )

    slug: str = Field('unique_slug',
        description='URL Friendly Post Title Slug',
        required=True,
    )

    title: str = Field('title',
        description='Post Title',
        required=True,
    )

    creator_id: int = Field('creator_id',
        description="Post Creator UserID",
        required=True,
    )

    # ForeignKey = many-to-one and inverse one-to-many
    # many-to-one = many posts can have ONE creator_id
    #   post.creator.id
    # one-to-many = inverse, one user can have many posts
    #   user.posts
    #   in django users.post_set.all()



    creator: Optional[User] = Field(None,
        description="Post Creator User Model",
        # ForeignKey or many-to-one
        # Default assumes foreign is 'id' and local is field + _id
        #has_one=(User),
        has_one=(User, 'id', 'creator_id'),
    )

    # comments: List[Comment] = Field(None,
    #     # One-to-Many (inverse so ForeignKey is actually on Comments table post_id)
    #     has_many=(Comment, 'post_id', 'id')
    # )

    # # On comments table - inverse
    # # posts: List[Post] = Field(None,
    # #     belongs_to=(Post, 'id', 'post_id')
    # # )

    # tags: List[Tag] = Field(None,
    #     # Many to many, requires a relation table like post_tags
    #     belongs_to_many=(Tag, 'post_tags', 'post_id', 'tag_id')
    # )

    # # On tags table
    # posts: List[Post] = Field(None,
    #     belongs_to_many=(Post, 'post_tags', 'tag_id', 'post_id')
    # )


    @property
    def creatorx(self):
        dd('hi')


# class Post(PostX, Model[PostX]):
#     pass

#x = Post(id=1, slug='asdf', title='asdf')
#dd(x)
#dd(Post.__dict__)
