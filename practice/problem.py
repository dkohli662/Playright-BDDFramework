

class Circle:
    def __init__(self, r):
        self.r=r
    def Area(self):
        a=3.14*self.r*self.r
        print("Area is :", a)
    def parameter(self):
        p=2*3.14*self.r
        print("perimeter is :", p)
obj=Circle(7)
obj.Area()
obj.parameter()



