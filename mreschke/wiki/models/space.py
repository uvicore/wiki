from __future__ import annotations

import uvicore
from typing import Optional, List
from uvicore.support.dumper import dd, dump
from uvicore.orm import Model, ModelMetaclass, HasMany, Field
from mreschke.wiki.database.tables import spaces as table


@uvicore.model()
class Space(Model['Space'], metaclass=ModelMetaclass):
    """Wiki Space Model"""

    # Database table definition
    __tableclass__ = table.Spaces

    id: Optional[int] = Field('id',
        primary=True,
        description='Space ID',
        read_only=True,
    )

    slug: str = Field('slug',
        description='URL Friendly Space Slug',
        required=True,
    )

    name: str = Field('name',
        description='Space Name',
        required=True,
    )

    order: int = Field('order',
        description='Space Display Order',
        required=True
    )

    # One-To-Many (One Space has Many Sections)
    sections: Optional[List[Section]] = Field(None,
        description='Space Sections Model',
        relation=HasMany('mreschke.wiki.models.Section', foreign_key='space_id')
    )


# Update forwrad refs (a work around to circular dependencies)
from mreschke.wiki.models.section import Section
Space.update_forward_refs()
