import pkg_resources

from .press import info, extract, run, press

__all__ = ["info", "extract", "run", "press"]

__version__ = pkg_resources.get_distribution(__name__).version
