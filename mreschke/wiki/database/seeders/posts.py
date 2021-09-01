import uvicore
import random
from uvicore import log
from faker import Faker
from mdgen import MarkdownPostProvider
from mreschke.wiki.models.post import Post
from uvicore.support.dumper import dump, dd

@uvicore.seeder()
async def seed():
    log.item('Seeding table posts')


    posts = []
    fake = Faker()
    fake.add_provider(MarkdownPostProvider)
    for _ in range(100):
        topic_id = random.randint(1, 15)
        title = fake.text(max_nb_chars=50)
        post = Post(
            slug=fake.slug(title),
            title=title,
            #body=fake.paragraph(nb_sentences=5),
            body=fake.post(size='large'),
            format_key='md',
            topic_id=topic_id,
            view_count=0,
            creator_id=1,
            updator_id=1,
        )
        #post.save()
        posts.append(post)




    # posts = []
    # fake = Faker()
    # for _ in range(100):
    #     topic_id = random.randint(1, 15)
    #     title = fake.text(max_nb_chars=50)
    #     post = Post(
    #         slug=fake.slug(title),
    #         title=title,
    #         body=fake.paragraph(nb_sentences=5),
    #         format_key='md',
    #         topic_id=topic_id,
    #         view_count=0,
    #         creator_id=1,
    #         updator_id=1,
    #     )
    #     #post.save()
    #     posts.append(post)





    #dump(posts)
    await Post.insert(posts)

