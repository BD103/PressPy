import os, time, ntpath, shutil
from zipfile import ZipFile

def extract(file):
  start = time.time()
  press = ntpath.basename(file)
  os.mkdir(press)
  zip = ZipFile(file, "r")
  zip.printdir()
  print("Extracting all files.")
  os.chdir(press)
  zip.extractall()
  end = time.time()
  print("Finished in", end - start, "seconds.")
  return press

def run(file, keep):
  press = extract(file)
  os.chdir(press)
  os.system("python main.py")
  os.chdir("../")
  if keep_file == False:
    shutill.rmtree(press)
