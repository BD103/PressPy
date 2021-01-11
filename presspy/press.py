import os
import time
import shutil
import json
import sys
import pkg_resources
from zipfile import ZipFile, ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA
import zlib
import bz2
import lzma


def info():
    print("PressPy Compression Software")
    print("Designed by BD103")
    print("Version: " + pkg_resources.get_distribution(__name__).version)
    print('Enter "presspy" for help')


def extract(file):
    # Starts timer
    start_time = time.time()

    # Extract program files
    print("Extracting program files")
    archive = ZipFile(file, "r")
    os.mkdir("program")
    os.chdir("program")
    archive.extractall()

    # Gets meta
    print("Reading meta file")
    with open("press.json", "r") as raw:
        meta = json.loads(raw.read())

    archive.close()

    # Installs dependencies
    print("Installing Dependencies")
    for i in meta["dependencies"]:
        os.system("pip install " + i)

    os.chdir("../")

    end_time = time.time()
    print("Process finished in " + str(end_time - start_time) + " seconds.")
    return meta


def run(file, keep):
    meta = extract(file)

    try:
        os.system("python program/" + meta["main"])
    except:  # noqa: E722
        print(
            "An error occured in the program. Please contact the developer.",
            file=sys.stderr,
        )

    if keep is False:
        shutil.rmtree("program")


def press(path):
    start_time = time.time()
    os.chdir(path)

    print("Reading press.json")
    with open("press.json") as raw:
        meta = json.loads(raw.read())

    include = []
    include.append(meta["main"])
    include.append("press.json")
    for i in meta["dependencies"]:
        if os.path.isfile(i):
            include.append(i)

    for i in meta["include"]:
        include.append(i)

    print("Writing .press file")
    if meta["zip_type"] == "STORED":
      compression_type = ZIP_STORED
    elif meta["zip_type"] == "DEFLATED":
      compression_type = ZIP_DEFLATED
    elif meta["zip_type"] == "BZIP2":
      compression_type = ZIP_BZIP2
    elif meta["zip_type"] == "LZMA":
      compression_type = ZIP_LZMA
    program = ZipFile("program.press", "w", compression_type)
    for i in include:
        program.write(i)
    program.close()

    end_time = time.time()
    print("Process finished in " + str(end_time - start_time) + " seconds.")
