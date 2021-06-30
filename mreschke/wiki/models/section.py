from __future__ import annotations

import uvicore
from typing import Optional, List
from uvicore.support.dumper import dd, dump
from uvicore.orm import Model, ModelMetaclass, HasMany, BelongsTo, Field
from mreschke.wiki.database.tables import sections as table


@uvicore.model()
class Section(Model['Section'], metaclass=ModelMetaclass):
    """Wiki Section Model"""

    # Database table definition
    __tableclass__ = table.Sections

    id: Optional[int] = Field('id',
        primary=True,
        description='Section ID',
        read_only=True,
    )

    slug: str = Field('slug',
        description='URL Friendly Section Slug',
        required=True,
    )

    name: str = Field('name',
        description='Section Name',
        required=True,
    )

    icon: str = Field('icon',
        description='Section Icon',
        required=False,
    )

    order: int = Field('order',
        description='Section Display Order',
        required=True
    )

    space_id: int = Field('space_id',
        description='Section SpaceID',
        required=True,
    )

    # One-To-Many (One Section has Many Topics)
    topics: 'Optional[List[Topic]]' = Field(None,
        description='Topics Model',
        relation=HasMany('mreschke.wiki.models.Topic', foreign_key='section_id')
    )

    # One-To-Many Inverse (One Section has one Space)
    space: 'Optional[Space]' = Field(None,
        description="Section Space Model",
        relation=BelongsTo('mreschke.wiki.models.Space')
    )


# Update forwrad refs (a work around to circular dependencies)
from mreschke.wiki.models.space import Space
from mreschke.wiki.models.topic import Topic
Section.update_forward_refs()
