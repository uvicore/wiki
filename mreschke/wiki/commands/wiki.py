from uvicore.support.click import click, typer, group_kargs
from .test import cli as test

# # Initialize click group for this app
# @click.group(**group_kargs)
# def cli():
#     """Wiki commands"""
#     pass


# cli.add_command(typer.main.get_command(test))


# import typer

# cli = typer.Typer(help="Blog Commands")

# @cli.command()
# def test():
#     """
#     Create a new user with USERNAME.
#     """
#     typer.echo(f"Test here")
