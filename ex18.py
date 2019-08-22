def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1,arg2))


def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1,arg2))


def print_one(arg1):
    print("arg1: {}".format(arg1))


def print_none():
    print("Such a nice day")

print_two("Some", "one")
print_two_again("One", "else")
print_one("to")
print_none()
