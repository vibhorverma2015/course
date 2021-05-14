class Animal:
    def __init__(self, name, no_of_legs, has_tails):
        self.name = name
        self.no_of_legs = no_of_legs
        self.has_tails = has_tails

    def eat(self):
        print(f"{self.name} is eating")

    def walk(self):
        print(f"{self.name} is walking")
