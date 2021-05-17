class Temperature:
    def __init__(self, temp):
        self.temp = 0
        pass

    def convert_celsius(self):
        print("changed from fahrenheit to celsius")

        print((fahrenheit-30)*5/9, "C")

    def convert_fahrenheit(self):
        print("changed from celsius to fahrenheit")
        print(celsius*1.8+32, "F")


print("temperature in celsius")
celsius = float(input())
temp = Temperature(celsius)
print(temp.convert_fahrenheit())

print("temperature in fahrenheit")
fahrenheit = float(input())
temp = Temperature(fahrenheit)
print(temp.convert_celsius())
