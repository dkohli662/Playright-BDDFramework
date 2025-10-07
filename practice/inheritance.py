from parent import Adder


class Child(Adder):
    b=100
    def Fun(self):
        print(return self.a + self.b)


obj=Child()
obj.Fun()



