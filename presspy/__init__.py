import sys

import pkg_resources

from .press import extract, lock, press, run

__all__ = ["extract", "run", "press", "lock"]

__version__ = pkg_resources.get_distribution(__name__).version


def info(file=sys.stdout):
    print("PressPy Compression Software", file=file)
    print("Designed by BD103", file=file)
    print(f"Version: {__version__}", file=file)
    print('Enter "presspy --help" for help', file=file)
