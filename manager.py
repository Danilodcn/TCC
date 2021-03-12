import click
from unittest import TestLoader, runner
from app import create_app

@click.group()
def command():
    ...

@command.command()
def runserver():
    app = create_app()
    app.run(port="100", debug=True)

@command.command()
def tests():
    loader = TestLoader()
    test = loader.discover("tests/")
    testrunner = runner.TextTestRunner()
    testrunner.run(test)

command()
