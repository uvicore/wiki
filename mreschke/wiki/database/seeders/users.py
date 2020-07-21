from faker import Faker
from ...models.user import User


def seed():
    users = []
    fake = Faker()
    for _ in range(2):
        user = User(name=fake.name())
        #user.name = fake.name()
        users.append(user)


    print(users)
