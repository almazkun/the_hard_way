the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "watermelon", "peach", "lime"]
change = [1, "25", 2, "50", 3, "75"]


for number in the_count:
    print("Counter: {}".format(number))


for fruit in fruits:
    print("Fruit: {}".format(fruit))


for i in change:
    print("I've got: {}".format(i))


element = []

for i in range(0, 6):
    print("Adding {} to list".format(i))
    element.append(i)
    print(element)


for i in element:
    print("Numbet or the item: {}".format(i))
    print(element)


print(element)
