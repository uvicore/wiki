import uvicore
from uvicore.support.click import click, group_kargs

@click.group(**group_kargs, help=f"""
    \b
    Uvicore 99.99
    A Fast Async ASGI Python Framework for CLI, Web and API
    Copyright (c) 2020 Matthew Reschke
    License http://mreschke.com/license/mit
""")
@click.version_option(version=99.99, prog_name='Uvicore2 Framework2', flag_value='--d')
def cli():
    pass
