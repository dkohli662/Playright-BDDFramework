class Student:
    college_name="Ramanujan college" # class variable
    name="annonymous"
    def __init__(self, name, marks):
        self.name=name # object variable / instance varthat will be different for everyone
        self.marks=marks
        print("adding new student")
s1=Student("Deepika", 98)
print(s1.name) # will always prefer obj variable not class var.
