from animal import Animal


class Dog(Animal):
    def __init__(self, name, no_of_legs, has_tails):
        print("dog constructor is called")
    super().__init__(name, no_of_legs, has_tails)

    def bark(self):
        print(f"{self.name} is barking")
