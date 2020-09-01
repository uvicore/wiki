from . import posts

def seed():
    # Order is critical for ForeignKey dependencies
    posts.seed()
