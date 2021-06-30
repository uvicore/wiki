import uvicore
from uvicore import log
from faker import Faker
from mreschke.wiki.models import Space
from uvicore.support.dumper import dump, dd


@uvicore.seeder()
async def seed():
    log.item('Seeding space')

    await Space.insert_with_relations([
        {
            'slug': '/it',
            'name': 'IT',
            'order': 1,
            'sections': [
                {
                    'slug': '/production',
                    'name': 'Production',
                    'icon': None,
                    'order': 1,
                    'topics': [
                        {
                            'slug': '/opennebula',
                            'name': 'OpenNebula',
                            'desc': 'Virtualization stack setup and documentation',
                            'icon': 'PhoneIcon',
                            'order': 1,
                        },
                        {
                            'slug': '/servers',
                            'name': 'Servers',
                            'desc': 'Physical and virtual servers with more really long comments',
                            'icon': 'PhoneIcon',
                            'order': 2,
                        },
                        {
                            'slug': '/networking',
                            'name': 'Networking',
                            'desc': 'Networking setup',
                            'icon': 'PhoneIcon',
                            'order': 3,
                        },
                    ]
                },
                {
                    'slug': '/branch',
                    'name': 'Branch Office',
                    'icon': None,
                    'order': 2,
                    'topics': [
                        {
                            'slug': '/dallas-office',
                            'name': 'Dallas Office',
                            'desc': 'Main headquarters with even more long comments because I ramble',
                            'icon': 'PhoneIcon',
                            'order': 1,
                        },
                        {
                            'slug': '/dallas-warehouse',
                            'name': 'Dallas Warehouse',
                            'desc': 'Main dallas warehouse',
                            'icon': 'PhoneIcon',
                            'order': 2,
                        },
                    ]
                },
                {
                    'slug': '/support',
                    'name': 'Support',
                    'icon': None,
                    'order': 3,
                    'topics': [
                        {
                            'slug': '/pc',
                            'name': 'PC',
                            'desc': 'PC Support and more really long comments',
                            'icon': 'PhoneIcon',
                            'order': 1,
                        },
                        {
                            'slug': '/phones',
                            'name': 'Phones',
                            'desc': 'Phone Support and whatnot and the other',
                            'icon': 'PhoneIcon',
                            'order': 2,
                        },
                        {
                            'slug': '/printers',
                            'name': 'Printers',
                            'desc': 'Printer Support because people cant figure that stuff out',
                            'icon': 'PhoneIcon',
                            'order': 3,
                        },
                    ]
                },
                {
                    'slug': '/something',
                    'name': 'Something',
                    'icon': None,
                    'order': 4,
                    'topics': [
                        {
                            'slug': '/this-and-that',
                            'name': 'This and That',
                            'desc': 'This and that long comments so I can see how it looks on the screen',
                            'icon': 'PhoneIcon',
                            'order': 1,
                        },
                        {
                            'slug': '/the-other',
                            'name': 'The Other',
                            'desc': 'The other, as in this that and the other like ol greg used to say',
                            'icon': 'PhoneIcon',
                            'order': 2,
                        },
                        {
                            'slug': '/some-son-beach',
                            'name': 'Some Son Beach',
                            'desc': 'Another one of ol gregs stupid sayings',
                            'icon': 'PhoneIcon',
                            'order': 3,
                        },
                    ]
                },
            ]
        },
        {
            'slug': '/dev',
            'name': 'Development',
            'order': 2,
            'sections': [
                {
                    'slug': '/apps',
                    'name': 'Applications',
                    'icon': None,
                    'order': 1,
                    'topics': [
                        {
                            'slug': '/wiki',
                            'name': 'Wiki',
                            'desc': 'Wiki application and more long comments just because',
                            'icon': 'PhoneIcon',
                            'order': 1,
                        },
                        {
                            'slug': '/tools',
                            'name': 'Tools',
                            'desc': 'Tools application and even longer comments still blah blah',
                            'icon': 'PhoneIcon',
                            'order': 2,
                        },
                    ]
                },
                {
                    'slug': '/languages',
                    'name': 'Languages',
                    'icon': None,
                    'order': 2,
                    'topics': [
                        {
                            'slug': '/python',
                            'name': 'Python',
                            'desc': 'Python language',
                            'icon': 'PhoneIcon',
                            'order': 1,
                        },
                        {
                            'slug': '/rust',
                            'name': 'Rust',
                            'desc': 'Rust language',
                            'icon': 'PhoneIcon',
                            'order': 2,
                        },
                    ]
                },
            ]
        },
    ])


        # # IT
        # {'slug': 'it/servers', 'section': 'IT', 'name': 'Servers', 'order': 1},
        # {'slug': 'it/opennebula', 'section': 'IT', 'name': 'OpenNebula', 'order': 2},
        # {'slug': 'it/networking', 'section': 'IT', 'name': 'Networking', 'order': 3},
        # #{'slug': 'it/shared', 'section': 'IT', 'name': 'Shared', 'order': 99},

        # # Development
        # {'slug': 'dev/apps', 'section': 'Development', 'name': 'Applications', 'order': 1},
        # {'slug': 'dev/python', 'section': 'Development', 'name': 'Python', 'order': 2},
        # {'slug': 'dev/rust', 'section': 'Development', 'name': 'Rust', 'order': 3},
        # #{'slug': 'it/shared', 'section': 'IT', 'name': 'Shared', 'order': 99},

        # # Support
        # {'slug': 'support/pc', 'section': 'Support', 'name': 'PC', 'order': 1},
        # {'slug': 'support/phone', 'section': 'Support', 'name': 'Phone', 'order': 2},


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

    #])
