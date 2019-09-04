people = 30
cars = 40
buses = 15


if cars > people:
    print("Lets drive")
elif cars < people:
    print("Lets walk")
else:
    print("Unable to choose!")


if buses > cars:
    print("Too many buses")
elif buses < cars:
    print("Shouldn't we be using a bus?")
else:
    print("Freedom is so hard!")


if people > buses:
    print("ok, go on bus")
else:
    print("Stying at home today!")
