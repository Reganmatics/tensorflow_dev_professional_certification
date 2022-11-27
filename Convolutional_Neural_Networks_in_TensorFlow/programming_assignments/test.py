import os
import shutil
import random
from shutil import copyfile

source_dir = os.getcwd()
print(f"current working directory is \n>>{source_dir}")
print(f"files in this directory are \n>>{os.listdir()}")


def list_zero_files(source):
    for file in source:
        if os.path.getsize(file) == 0:
            print(f"the file {file} is empty")
        else:
            print("this is a normal image")

def main():
    source = "./tmp/PetImages"
    print(list_zero_files(source))

main()
