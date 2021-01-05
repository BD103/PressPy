import click
import presspy


@click.group()
def cli():
    "A Python Project Compression Software"
    pass


@cli.command()
@click.argument("file")
@click.option(
    "--keep",
    default=False,
    is_flag=True,
    help="Keeps the source program after running in a folder.",
)
def run(file, keep):
    "Runs a .press file."
    print("Running")
    presspy.run(file, keep)


@cli.command()
@click.argument("path")
def press(path):
    "Presses a Python program into a .press file."
    presspy.press(path)


@cli.command()
@click.argument("file")
def extract(file):
    "Puts source of .press file into folder."
    presspy.extract(file)
