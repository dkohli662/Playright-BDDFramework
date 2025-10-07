class myClass :
    num=5
    def getData(self):
        print("my method")
    def __init__(self):
        print("construct call with object creation")
obj=myClass()
print(obj.num)
obj.getData()