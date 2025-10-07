print("Hello Deepika")
# comment syntax in python

#declare varaiables

a=4
name="Deepika"
number=4.55
print(a, name, number)

# multi type variables in a single line
b,c,d = 5,5.5,"Test"
print(b,c,d)

# , is used to concatanate
print("value of b is", b)

# to know data type of any variable

print(type(b))
print(type(name))

# + is used to concatanate two or more strings but can't be used for different data types

List=[3, 4.55, "Test", 67]
print(List[0]) # 3
print(List[2]) # test

# slicing - print sublist of main list - last index not include3d

print(List[1:3])

# insert valuse in list

List.insert(2, 45)


# update list value
List[2] = "Deepika"

# deleting value from list

del List[0]
print(List)

