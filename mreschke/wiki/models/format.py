from __future__ import annotations

import uvicore
from typing import Optional
from uvicore.support.dumper import dd, dump
from uvicore.orm import Model, ModelMetaclass, BelongsTo, Field
from mreschke.wiki.database.tables import formats as table


@uvicore.model()
class Format(Model['Format'], metaclass=ModelMetaclass):
    """Wiki Format Model"""

    # Database table definition
    __tableclass__ = table.Formats

    key: str = Field('key',
        primary=True,
        description='Format Key',
    )

    name: str = Field('name',
        description='Format name',
        required=True,
    )
