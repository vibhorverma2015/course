from .class_student import Student  # importing

if __name__ == "__main__":
    kunal = Student("Kunal chopra", 21, 2000)

    abhijeet = Student("Abhijeet Singh", 19, 2001)

    print(kunal.name)
    print(kunal.age)
    print(kunal.birth_year)

    kunal.read()
    kunal.write()
    kunal.mcq("Tuples")

    print(abhijeet.name)
    abhijeet.read()
    abhijeet.topic()
    abhijeet.mcq("Oops")
