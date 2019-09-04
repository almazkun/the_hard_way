from sys import argv
from pathlib import Path
from os.path import exists


script, from_file, to_file = argv


print("Copying content of the {} file to the {} file".format(from_file, to_file))


with open(from_file, "br") as indate:
    indate = indate.read()
    indate = str(indate, "UTF-8")

print("File {} size is {} byites.".format(from_file, len(from_file)))
print("Is file exist? {}".format(exists(to_file)))
print("I am ready to be done with it.")
input("Press 'Enter' to continiue. Press 'Ctrl + C' to cancel.")

with open(to_file, "w") as todate:

    todate.write(indate)

print("\nDONE\n")
