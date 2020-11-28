import uvicore
from . import posts

@uvicore.seeder()
async def seed():
    # Order is critical for ForeignKey dependencies
    await posts.seed()
