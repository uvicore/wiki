import uvicore
from uvicore import log
from faker import Faker
from mreschke.wiki.models.post import Post
from uvicore.support.dumper import dump, dd

@uvicore.seeder()
async def seed():
    log.item('Seeding table posts')
    posts = []
    fake = Faker()
    for _ in range(2):
        title = fake.text(max_nb_chars=50)
        post = Post(
            slug=fake.slug(title),
            title=title,
            body=fake.paragraph(np_sentences=5),
            format_key='md',
            creator_id=1,
            updator_id=1,
        )
        #post.save()
        posts.append(post)

    await Post.insert(posts)
    #dump(posts)