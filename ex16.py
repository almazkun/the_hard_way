from sys import argv

script, filename = argv


print("I will delete file {}".format(filename))
print("If you don't want to this: press 'Ctrl + C'")
print("if you want me to do this: press 'Enter'")
input("?")

print("Opening file...")
target = open(filename, "w")

print("Cleanin the file {}. Chao!!".format(filename))

print("Now, I will ask you to provide me with three lines.")

line1 = input("Line #1: ")
line2 = input("Line #2: ")
line3 = input("Line #3: ")

print("This lines will be added to the file {}.".format(filename))

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("Closing file {}. Saionara!".format(filename))
target.close