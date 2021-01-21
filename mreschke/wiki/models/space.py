from __future__ import annotations

import uvicore
from typing import Optional
from uvicore.support.dumper import dd, dump
from uvicore.orm import Model, ModelMetaclass, BelongsTo, Field
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

    section: str = Field('section',
        description='Space Section',
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
