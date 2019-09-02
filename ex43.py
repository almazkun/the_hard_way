from sys import exit
from random import randint


class Scene:
    def enter(self):
        print("This scene is not defined yet, subclass it and create enter() function.")

        exit(1)


class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    quips = ["GAME OVER", "GAME IS OVER", "THE GAME IS OVER", "THE GAME IS THE OVER"]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print(
            """
    Gots have taken over your ship and killed everyone except for you.
    You need to steal Neutron Bomb in laboratory and put it into Fuel Cell.
    And try to escape the ship before its explods.        
            """
        )
        print("\n")
        print(
            "You are in the Central Corridor and faced with Got. He is being ready to shoot you whith the blaster."
        )
        print("\n")
        print("What will you do?")

        action = input("===>")

        if "shoot" in action:
            print(
                "He is too small and lurky. You try to hit him but all shoots are missed. And Got is head shotted you!"
            )
            return "death"

        elif "run" in action:
            print(
                "You try to run faster and bypass him from the right. But this what he was waiting for. He headshooted you!"
            )
            return "death"

        elif "joke" in action:
            print(
                "You know Gots very well and you know that you can make them laugh. You make a choke and Gots starts to laugh very hard and shoot him in the head and turn to the Laboratory."
            )
            return "laser_weapon_armory"

        else:
            print("Hm, smart but not enought. Try again.")
            return "central_corridor"


class LaserWeaponArmory(Scene):
    def enter(self):
        print(
            """
        You are entering Armory. It is dead quit inside. 
        You run to the secret loker room. It is where the Neutron bomb is hidden.
        You found the box with the bomb! But it is locked!
        You need to enter 3 digit code to open it.
        Be carefull after 10 wrong entrings box will be locked forever!
        Good luck to you me lucky guesser! 
            """
        )
        code = "{}{}{}".format(randint(0,9), randint(0,9), randint(0,9))
        print(code)
        guess = input("""
            | 7 | 8 | 9 | 
            --- --- --- 
            | 4 | 5 | 6 |
            --- --- --- 
            | 1 | 2 | 3 |
            --- --- --- 
            | 0 | open> |
            _____________
            | * | * | * | >
            """ 
        )
        guesses = 0

        while guess!= code and guesses < 9:
            print("Piii piii piii Wrong Code!")
            guesses += 1
            print(9 - guesses, "left")
            input("""
            | 7 | 8 | 9 | 
            --- --- --- 
            | 4 | 5 | 6 |
            --- --- --- 
            | 1 | 2 | 3 |
            --- --- --- 
            | 0 | open> |
            _____________
            | * | * | * | >
            """ 
            )

        if guess == code:
            print("FUUUUUUSSSSSSHHHHHHsssss")
            print("Box opens with pleasent fuushing sound")
            print(
            """
        Luck is on our side today!
        You grab the bomb and run to the most vulnerable place of the battleship.
            """
            )
            return "the_fuel_cell"
        else:
            print("""
        You hear the last error message and see the melting of the lock. 
        Neutron bomb is forever safe in the unopenanable box.
        You lost in despair in your battleship and met your death there when God exploded it.
            """
            )
            return "death"


class TheFuelCell(Scene):
    def enter(self):
        print("""
        You run into Fuel Cell room and see 5 Gods There. 
        They all see you and Neutron bomb. 
        They are unsure and motionless.
        What will you do?
        """)
        print("\n")
        print("What will you do?")
        action = input("===>")

        if "run away" in action:
            print("You try to run away, but they shoot you in the back")
            return "death"
        elif "setup" in action:
            print("You setup bomb in the Fuel Cell and run to the Escape Pods")
            return "escape_pod"
        else:
            print("Hm, smart, but not enought. Try something better this time.")
            return "the_fuel_cell"


class EscapePod(Scene):
    def enter(self):
        print("""
        You have run up to Escape pods. 
        You know that some of them have been demaged in the battle with Gots and will explode after start!
        You have no time to check them all. You neet to guess on and pray for the luck!
        """)
        good_pod = randint(1, 5)
        print("Which one will you chose")
        print(good_pod)
        guess = input("""
            | 1 | 2 | 3 | 4 | 5 |
            _____________________
            | * |>
            """ 
        )

        if int(guess)!= good_pod:
            print("""
        You choose {}, but should have choosen {}
            """.format(guess, good_pod))
            return "death"
        else:
            print("You won!")
            return "finished"


class Finished(Scene):
    def enter(self):
        print("You Won! Congratulations!")
        return "finished"


class Map:


    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_fuel_cell": TheFuelCell(),
        "escape_pod": EscapePod(),
        "death": Death(),
        "finished": Finished(),
    }


    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val


    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
