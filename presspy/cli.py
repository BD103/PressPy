import os, click
import presspy


@click.group()
def cli():
    pass


@cli.command()
@click.argument("file")
@click.option("--keep", default=False, is_flag=True, help="Keeps the source program after running in a folder.")
def run(file):
    "Runs a .press file."
    print("Running")
    presspy.run(file)

@cli.command()
@click.argument("path")
@click.option("--main", default="main.py", help="The main file to scan")
def press(path, main):
    "Presses a Python program into a .press file."
    print("Pressing.")
