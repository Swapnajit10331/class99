import os
import shutil

source=input("enter source folder name:")
destination=input("enter destination folder name:")

source=source+"/"
destination=destination+"/"

listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)
