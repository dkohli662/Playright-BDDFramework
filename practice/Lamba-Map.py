numbers= [2, 5, 3, 4, 6]

# multipel each item by 2 and return list

squared_num= map(lambda x : x*2, numbers)

print(list(squared_num))

# extract even numbers from list in form of another list

even_num=list(filter(lambda x : x%2==0, numbers))
print(even_num)

even_num1=list(map(lambda x : x%2==0, numbers))

print(even_num1)


