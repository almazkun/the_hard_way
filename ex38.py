ten_things = "Apples Oranges Cross Telephone Light Sugar"

print("Wait a minute, There shpuld be 10 items! Let's fix it!")

stuff = ten_things.split(" ")

more_stuff = ["Day", "Night", "Song", "Flisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff)!= 10:
    next_one = more_stuff.pop()
    print("Add: {}".format(next_one))
    stuff.append(next_one)
    print("This is what we have now: {}, and number of objects are {}".format(stuff, len(stuff)))


print("This is what we have in the end: {}".format(stuff))


print("Let's do something with them")


print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))
