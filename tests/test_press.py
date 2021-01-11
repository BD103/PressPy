import os
import unittest

import presspy

# import pytest

"""
class Template:
    def __init__(self):
        self.main = "f = open('file.txt', 'rt')\nwith open('stream.txt', 'wt') as stream:\n\tprint(f.read(), file=stream)"
        self.text = "PressPy is cool"
        self.config = {"main": "main.py", "include": ["file.txt"]}

    def create(self):
        with open("tests/main.py", "wt") as main:
            main.write(self.main)
        with open("tests/text.txt", "wt") as module:
            module.write(self.text)
        with open("tests/press.json", "wt") as config:
            config.write(json.dumps(self.config))
"""


class Main(unittest.TestCase):
    def test_info(self):
        with open("stream.txt", "wt") as stream:
            presspy.info(file=stream)
        version = presspy.__version__
        expected = f"""
PressPy Compression Software
Designed by BD103
Version: {version}
Enter "presspy --help" for help
"""
        with open("stream.txt", "rt") as stream:
            assert stream.read().strip() == expected.strip()
        os.remove("stream.txt")


class CLI(unittest.TestCase):
    def test_none(self):
        assert None is None
