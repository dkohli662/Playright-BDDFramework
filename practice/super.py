class A:
    def display(self):
        print("I am the parent class")

class B(A):
    def display(self):
        super().display()  # Call parent class method
        print("I am the child class")
obj=B()
obj.display()
