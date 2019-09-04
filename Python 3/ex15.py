from sys import argv

script, filename = argv


txt = open(filename)
print("File content: {}".format(filename))
print("\n" + txt.read() + "\n")
txt.close()


print("Enter the name of the file, again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
