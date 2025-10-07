# fibonacci series until 10--> 0, 1, 1, 2, 3, 5, 8...

def fib():
    a, b=0, 1
    print(a, b, end=" ")
    for i in range(10):
        c=a+b
        print(c, end=" ")
        a=b
        b=c
fib()






