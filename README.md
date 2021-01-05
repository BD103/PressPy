# PressPy

A Python compression software.

## Intallation

Intall with Pip:
```console
pip install --upgrade presspy
```

Install latest Github version:
**May have many bugs!**
```console
pip install --upgrade git+https://github.com/BD103/presspy
```

## How to Use

PressPy is purely console based. Open up command prompt, or another console likewise, and type `presspy`.
This gives you a list of available commands and options. There are three main functions:

### Run

Runs a `.press` file.

Usage:
```
presspy run file --keep
```

File:
The location of your `.press` file relative to your current directory.

--keep:
Use this flag if you wish to keep the extracted source after running.

### Press

Presses a Python program into a `.press` file.

Usage:
```
presspy press path
```

Path:
The folder or directory your source code is in relative to your current directory. This folder must contain a press.json file. See the [Wiki](https://github.com/BD103/PressPy/wiki) for more information.

### Extract

Puts the source of a `.press` file into a folder.

Usage:
```
presspy extract file
```

File:
The location of your `.press` file relative to your current directory.

## Contributing

After editing the code, run it through our checks:
```console
pip install -r requirements.txt
black presspy tests
flake8
pytest
```

Black should return something along the lines of:
```console
All done! ✨ 🍰 ✨
1 file reformatted, 3 files left unchanged.
```

Flake8 should return any other formatting errors and a count, so you should see:
```console
0
```

Last, Pytest should tell you:
```console
==================== test session starts ====================
platform linux -- Python 3.8.7, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /home/runner/PressPy
collected 2 items

tests/test_presspy.py ..                              [100%]

===================== 2 passed in 0.20s =====================
```

Once you don't have any errors, create a pull request. We will soon check it over! Thanks for contributing! Github also checks over PR to the Main branch with Github Actions, just to double check.
