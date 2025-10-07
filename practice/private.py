class Person:
    __name="annonymous"  # private var
    def __hello(self): # private method
        print("hello person")

    def welcome(self): # non private methode to call private method
        self.__hello()
obj=Person()
obj.welcome()