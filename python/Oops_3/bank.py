class Bank:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def add_amount(self, x):
        self.amount += x


class HDFC(Bank):
    def __init__(self):
        name = "HDFC"
        super().__init__(name)


if __name__ == "__main__":
    bank = HDFC()
    bank.add_amount(100)
    print(bank.name)
    print(bank.amount)


class AXIS(Bank):
    def __init__(self):
        name = "AXIS"
        super().__init__(name)


if __name__ == "__main__":
    bank = AXIS()
    bank.add_amount(5000)
    print(bank.name)
    print(bank.amount)
