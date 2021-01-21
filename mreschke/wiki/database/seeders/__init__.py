import uvicore


@uvicore.seeder()
async def seed():
    # Import seeders
    from . import format, post, space

    # Run seeders. Order is critical for ForeignKey dependencies
    await format.seed()
    await space.seed()
    #await post.seed()
