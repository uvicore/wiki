import uvicore
from uvicore import log
from faker import Faker
from mreschke.wiki.models import Format
from uvicore.support.dumper import dump, dd


@uvicore.seeder()
async def seed():
    log.item('Seeding format')
    await Format.insert([
        {'key': 'md', 'name': 'Markdown'},
        {'key': 'htm', 'name': 'HTML'},
        {'key': 'txt', 'name': 'Text'},
    ])
