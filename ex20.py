from sys import argv


script, inpute_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(inpute_file)


print("First of all print all file:\n")


print_all(current_file)


print("Now backwards:\n")


rewind(current_file)


print("Now print 3 lines:")


current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)