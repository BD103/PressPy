import pkg_resources

from .press import extract, info, lock, press, run

__all__ = ["info", "extract", "run", "press", "lock"]

__version__ = pkg_resources.get_distribution(__name__).version
