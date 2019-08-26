from sys import exit


def gold_room():
    print("It is a room full of gold, how much can you take away?")

    next = input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        daed("You need inter a number")
    

    if how_much < 50:
        print("Wonderful! You can take it home!")
        exit(0)
    else:
        dead("You greedy bastard!")
    

def bear_room():
    print("""
    Room of Sleeping Bear is upon you to enjoy.
    Sleeping bear is blocking the exit door.
    What are you going to do? 
    Poke a bear or take away honey?
    """)
    bear_moves = False


    while True:
        next = input("> ")

        if next == "Take away honey":
            dead("Bear had eaten your head.")
        elif next == "Poke a bear" and not bear_moves:
            print("""
            Bear opened the door.
            Poke a bear or enter the door?
            """)
            bear_moves = True
        elif next == "Poke a bear" and bear_moves:
            dead("You pissed of the bear and it eats you!")
        elif next == "enter the door" and bear_moves:
            gold_room()
        else:
            print("I have no idea what's going on")


def chtulhu_room():
    print("""
    You are on the edge of the abbysse!
    Run away or eat your own head?
    """)
    next = input("> ")


    if "away" in next:
        start()
    elif"head" in next:
        dead("Its seems like you have eaten your own head.")
    else:
        chtulhu_room()
    

def dead(why):
    print(why, "Wonderful!")
    exit(0)


def start():
    print("""
    You are in Dark Room of choislessness.
    You are faced with two doors. 
    Which one you choose? Left or right?
    """)
    next = input("> ")


    if "eft" in next:
        bear_room()
    elif "ight" in next:
        chtulhu_room()
    else:
        dead("Starvation death!")


start()
