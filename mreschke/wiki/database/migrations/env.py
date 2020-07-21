from alembic import context

config = context.config

#from ...models import user
from mreschke.wiki.models.user import User

from uvicore.db import Model
target_metadata = Model.metadata
