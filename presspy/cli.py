import os, click
import presspy


@click.group()
def cli():
    pass


@cli.command()
@click.argument("file")
@click.option("--keep", default=False, is_flag=True)
def run(file):
    "Runs a .press file."
    print("Running")
    presspy.run(file)

@cli.command()
@click.argument("file")
def press(file):
    "Presses a Python program into a .press file."
    print("Pressing.")
