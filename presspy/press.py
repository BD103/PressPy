import os, time, ntpath, shutil, json, sys
from zipfile import ZipFile


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
    print("Process finished in " + end_time - start_time + " seconds.")
    return meta


def run(file, keep):
    meta = extract(file)

    try:
        os.system("python program/" + meta["main"])
    except:
        print(
            "An error occured in the program. Please contact the developer.",
            file=sys.stderr,
        )

    if keep == False:
        shutil.rmtree("program")


def press(path):
    start_time = time.time()
    os.chdir(path)

    print("Reading press.json")
    with open("press.json") as raw:
        meta = json.loads(raw.read())

    include = []
    include.append(meta["main"])
    for i in meta["dependencies"]:
        if os.path.isfile(i):
            include.append(i)

    for i in meta["include"]:
        include.append(i)

    print("Writing .press file")
    program = ZipFile("program.press", mode="w")
    for i in include:
        program.write(i)
    program.close()

    end_time = time.time()
    print("Process finished in " + end_time - start_time + " seconds.")
