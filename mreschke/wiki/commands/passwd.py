import uvicore
from uvicore.support.dumper import dump, dd
from uvicore.console import command, argument, option


@command()
async def cli():
    """Wiki passwd CLI command"""

    from uvicore.auth.support import password
    pwd = "techie1234"
    x = password.create(pwd)
    print("Password: {}".format(pwd))
    print()
    print(x)
