a=int(input("enter a"))
b=int(input("enter b"))

try:
    print("result is :", a/b) # will execute if no exception
except ZeroDivisionError as e:
    print("deivision by 0 is not possible :", e) # will execute if exception occurs & e will print error text
finally: # will always execute
    print("end of code")
