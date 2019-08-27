class Animal():
    pass


class Dog(Animal):
    def __init__ (self, name):
        self.name = name

    
    def bark(self, times):
        print("Gav " * times)

