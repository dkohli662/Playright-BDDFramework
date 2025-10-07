class BasicCalculator:
    def __init__(self):
        self.a = 10
        self.b = 5

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


obj = BasicCalculator()
print("Addition: 10 + 5 =", obj.add())
print("Subtraction: 10 - 5 =", obj.sub())
print("Multiplication: 10 * 5=", obj.mul())
print("Division: 10 / 5=", obj.div())





