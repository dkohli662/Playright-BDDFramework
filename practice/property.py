class Student:
    def __init__(self, P, C, M):
        self.P=P
        self.C=C
        self.M=M
    @property # property decorator
    def percentage(self):
        return str((self.P + self.C + self.M)/3)
obj=Student(98, 76, 54)
print(obj.percentage)

obj.P=75
print(obj.percentage)

