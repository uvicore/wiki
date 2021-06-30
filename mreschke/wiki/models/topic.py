from __future__ import annotations

import uvicore
from typing import Optional
from uvicore.support.dumper import dd, dump
from uvicore.orm import Model, ModelMetaclass, BelongsTo, Field
from mreschke.wiki.database.tables import topics as table


@uvicore.model()
class Topic(Model['Topic'], metaclass=ModelMetaclass):
    """Wiki Topic Model"""

    # Database table definition
    __tableclass__ = table.Topics

    id: Optional[int] = Field('id',
        primary=True,
        description='Topic ID',
        read_only=True,
    )

    slug: str = Field('slug',
        description='URL Friendly Topic Slug',
        required=True,
    )

    name: str = Field('name',
        description='Topic Name',
        required=True,
    )

    desc: str = Field('desc',
        description='Topic Description',
        required=False,
    )

    icon: str = Field('icon',
        description='Topic Icon',
        required=False,
    )

    order: int = Field('order',
        description='Topic Display Order',
        required=True
    )

    section_id: int = Field('section_id',
        description='Topic SectionID',
        required=True,
    )

    # One-To-Many Inverse (One Section has one Space)
    section: 'Optional[Section]' = Field(None,
        description="Topic Section Model",
        relation=BelongsTo('mreschke.wiki.models.Section')
    )


# Update forwrad refs (a work around to circular dependencies)
from mreschke.wiki.models.section import Section
Topic.update_forward_refs()
