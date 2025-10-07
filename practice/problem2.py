class Emp:
    def __init__(self, role, dept, salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role is :", self.role)
        print("dept is :", self.dept)
        print("salary is :", self.salary)

obj=Emp("manager", "IT", 50000)
obj.showDetails()

class Engineer(Emp): # child class of Emp
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("engineer", "IT", 80000) # inheri parent attributes
    def show(self):
        print("role is :", self.role)
        print("dept is :", self.dept)
        print("salary is :", self.salary)
        print("name is :", self.name)
        print("age is :", self.age)
eng=Engineer("Deepika Kohli", 25)
eng.show()



