print("You are in the dark room woth two doors. You need to choose door 1 or 2.")
door = input("> ")

if door == "1":
    print(
        "There is a GIANT BLACK BEAR in the room eating cheese cake. What will you do?"
    )
    print("1. Take cheese cake.")
    print("2. Screem into Bear's ears.")
    bear = input("> ")

    if bear == "1":
        print("Bear eaten your head! Nice jod!")
    elif bear == "2":
        print("Bear eaten your leg! Good!")
    else:
        print("Bear run away, for some misterious reason.")
elif door == "2":
    print("You are looking into abysse. What would you do?")
    print("1. Screem your name into abysse.")
    print("2. Fasten you seatbelt.")
    print("3. Spit into it")
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your are saved, because abysse is deeply heart")
    else:
        print("You gone insane and jumped into the pool of some dicusting supstanse.")
else:
    print("You woken up, it was a dream, everyting is fine, poor little bear!")
