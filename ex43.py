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
            return "Death()"

        elif "run" in action:
            print(
                "You try to run faster and bypass him from the right. But this what he was waiting for. He headshooted you!"
            )
            return "Death()"

        elif "joke" in action:
            print(
                "You know Gots very well and you know that you can make them laugh. You make a choke and Gots starts to laugh very hard and shoot him in the head and turn to the Laboratory."
            )
            return "LaserWeaponArmory()"

        else:
            print("Hm, smart but not enought. Try again.")
            return "CentralCorridor()"


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

        while guess!= code and guesses < 10:
            print("Piii piii piii Wrong Code!")
            guesses += 1
            print(10 - guesses, "left")
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
        return "TheFuelCell()"


class TheFuelCell(Scene):
    def enter(self):
        pass


class EscapePod(Scene):
    def enter(self):
        pass


class Map:
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play

a = LaserWeaponArmory()
a.enter()