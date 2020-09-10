from . import posts

async def seed():
    # Order is critical for ForeignKey dependencies
    await posts.seed()
