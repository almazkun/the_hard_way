def add(a, b):
    print("Adding {} + {}".format(a, b))
    return a + b


def subtrackt(a, b):
    print("Subtrackting {} - {}".format(a, b))
    return a - b


def multiply(a, b):
    print("Multyplying {} * {}".format(a, b))
    return a * b


def divide(a, b):
    print("Dividing {} / {}".format(a, b))
    return a / b


print("Let's make some calculations\n")
age = add(30, 7)
height = subtrackt(190, 4)
weight = multiply(35, 2)
iq = divide(220, 2)


print(
    "Age: {} years, height: {} santimetres, weight: {} kilograms, iq: {} or negligible.\n".format(
        age, height, weight, iq
    )
)


print("It is interesting: ")

what = add(age, subtrackt(height, multiply(weight, divide(iq, 2))))
print("Result: ", what, "Can you calculate that manualy?")
