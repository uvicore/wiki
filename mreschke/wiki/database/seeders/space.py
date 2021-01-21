import uvicore
from uvicore import log
from faker import Faker
from mreschke.wiki.models import Space
from uvicore.support.dumper import dump, dd


@uvicore.seeder()
async def seed():
    log.item('Seeding space')
    await Space.insert([

        # IT
        {'slug': 'it/production', 'section': 'IT', 'name': 'Production', 'order': 1},
        {'slug': 'it/tech-support', 'section': 'IT', 'name': 'Tech Support', 'order': 2},
        {'slug': 'it/development', 'section': 'IT', 'name': 'Development', 'order': 3},
        {'slug': 'it/shared', 'section': 'IT', 'name': 'Shared', 'order': 99},

        # Residential
        {'slug': 'residential/operations', 'section': 'Residential', 'name': 'Operations', 'order': 100},
        {'slug': 'residential/sales', 'section': 'Residential', 'name': 'Sales', 'order': 101},
        {'slug': 'residential/marketing', 'section': 'Residential', 'name': 'Marketing', 'order': 102},
        {'slug': 'residential/shared', 'section': 'Residential', 'name': 'Shared', 'order': 199},

        # Commercial
        {'slug': 'commercial/operations', 'section': 'Commercial', 'name': 'Operations', 'order': 200},
        {'slug': 'commercial/sales', 'section': 'Commercial', 'name': 'Sales', 'order': 201},
        {'slug': 'commercial/marketing', 'section': 'Commercial', 'name': 'Marketing', 'order': 202},
        {'slug': 'commercial/shared', 'section': 'Commercial', 'name': 'Shared', 'order': 299},

        # Company
        {'slug': 'company/hr', 'section': 'Company', 'name': 'Human Resources', 'order': 300},
        {'slug': 'company/shared', 'section': 'Company', 'name': 'Shared', 'order': 399},

    ])
