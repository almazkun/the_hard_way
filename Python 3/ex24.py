print("Lets have some practice")
print(
    "You need to know about special caracter \\, whish \ncontrol lines, and \ttabulations"
)


poem = """
I need not much
I want to tenderly \n hold you in my hand,
I forever
be with you
\n\t\tAnd never let you go!
"""


print("_____________")
print(poem)
print("_____________")


five = 10 - 2 + 3 - 6
print("It must be five: {}.".format(five))


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1
beans, jars, crates = secret_formula(start_point)


print("Starting with: {}.".format(start_point))
print("We have {} beans, {} jars and {} boxes.".format(beans, jars, crates))


start_point = start_point / 10
print("We can do the following way:")
print("We have {} beans,  jars and  boxes.".format(secret_formula(start_point)))
