def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {} bottles of cheese.\nYou have {} boxes of crackers.\nIt is more than enought for a party.\nPOEHALI!\n".format(cheese_count, boxes_of_crackers))


print("We can assign arguments direcly:")
cheese_and_crackers(200, 500)


print("Or we can assign them through variables")
amount_of_cheese = 99899
amount_of_crackers = 99799
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("we can even use calculations inside of the function call")
cheese_and_crackers(125456252*54151515168486946, 4848461598491653135121**55)


print("and combine variables with calculations")
cheese_and_crackers(amount_of_cheese**5, amount_of_crackers**55)
