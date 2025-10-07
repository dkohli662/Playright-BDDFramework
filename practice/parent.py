class Adder:
    a=200
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

# Create an object with two numbers
obj = Adder(10, 170)

# Call the add method and print the result
result = obj.add()
print("Sum:", result)
