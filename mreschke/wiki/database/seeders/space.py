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
        {'slug': 'it/servers', 'section': 'IT', 'name': 'Servers', 'order': 1},
        {'slug': 'it/opennebula', 'section': 'IT', 'name': 'OpenNebula', 'order': 2},
        {'slug': 'it/networking', 'section': 'IT', 'name': 'Networking', 'order': 3},
        #{'slug': 'it/shared', 'section': 'IT', 'name': 'Shared', 'order': 99},

        # Development
        {'slug': 'dev/apps', 'section': 'Development', 'name': 'Applications', 'order': 1},
        {'slug': 'dev/python', 'section': 'Development', 'name': 'Python', 'order': 2},
        {'slug': 'dev/rust', 'section': 'Development', 'name': 'Rust', 'order': 3},
        #{'slug': 'it/shared', 'section': 'IT', 'name': 'Shared', 'order': 99},

        # Support
        {'slug': 'support/pc', 'section': 'Support', 'name': 'PC', 'order': 1},
        {'slug': 'support/phone', 'section': 'Support', 'name': 'Phone', 'order': 2},


        # # Residential
        # {'slug': 'residential/operations', 'section': 'Residential', 'name': 'Operations', 'order': 100},
        # {'slug': 'residential/sales', 'section': 'Residential', 'name': 'Sales', 'order': 101},
        # {'slug': 'residential/marketing', 'section': 'Residential', 'name': 'Marketing', 'order': 102},
        # {'slug': 'residential/shared', 'section': 'Residential', 'name': 'Shared', 'order': 199},

        # # Commercial
        # {'slug': 'commercial/operations', 'section': 'Commercial', 'name': 'Operations', 'order': 200},
        # {'slug': 'commercial/sales', 'section': 'Commercial', 'name': 'Sales', 'order': 201},
        # {'slug': 'commercial/marketing', 'section': 'Commercial', 'name': 'Marketing', 'order': 202},
        # {'slug': 'commercial/shared', 'section': 'Commercial', 'name': 'Shared', 'order': 299},

        # # Company
        # {'slug': 'company/hr', 'section': 'Company', 'name': 'Human Resources', 'order': 300},
        # {'slug': 'company/shared', 'section': 'Company', 'name': 'Shared', 'order': 399},

    ])
