from faker import Faker
from mreschke.wiki.models.user import User
from uvicore.support.dumper import dump, dd

def seed():
    users = []
    fake = Faker()
    for _ in range(2):
        user = User(name=fake.name())
        users.append(user)

    dump(users)
