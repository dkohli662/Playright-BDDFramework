class A:
    @classmethod
    def class_method(cls):
        return "class"

    def instance_method(self):
        return "instance"
obj=A()
print(obj.instance_method())
print(A.class_method()) # classname is use to call class methods
