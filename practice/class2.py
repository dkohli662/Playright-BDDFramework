# print the name and avg score of 3 subjects of a student
# marks will be taken in form of list
class Student:
    @staticmethod
    def display():
        print("student records gets displayed")
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        s=0
        for i in self.marks:
            s=s+i
        print("Hi", self.name, "your avg score is", s/3)
obj=Student("Deepika Kohli", [99, 98, 96])
obj.get_avg()
obj.display()


