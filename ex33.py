i = 0
numbers = []


while i < 6:
    print("Item before {}.".format(i))
    numbers.append(i)

    i += 1
    print("Current items: {}".format(numbers))
    print("Item after {}".format(i))


print("Item: ")
for num in numbers:
    print(num)
