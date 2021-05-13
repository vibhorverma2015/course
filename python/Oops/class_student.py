class Student:
    def __init__(self, age, birth_year):  # constructor/ dunder init
        pass

        self.name = "Kunal Chopra"
        self.age = age
        self.birth_year = birth_year

    def read(self):
        print(f"student {self.name} is reading")

    def write(self):
        print(f"student {self.name} is writing")

    def mcq(self, topic):
        print(f"student{self.name} gave the mcq of topic {topic}")
