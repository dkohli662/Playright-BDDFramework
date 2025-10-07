List=[4, "Deepika", 56.66, 900]
print(List)
print(List[1])

List.append("Test")
print(List)

List.insert(1, 100)
print(List)
del List[3]
print(List)

List[2]="Kohli"  # replacing value of index 2
print(List)

List2=[55, 30, 50, 67, 89, 23]
List2.sort() # sort in accending order
print(List2)

List2.reverse() # print reversed list from last index till 0th index
print(List2)

List2.remove(30) # will reomove 30 from list
List2.pop(0) # remove item of index 0
print(List2)

print(List2[1:3])  # slicing

tuple=(1,34,53,0,35) # tuple immutable in nature.can not be changed
print(tuple)

# ditionary - key can be string or int all string should come in "" whether they are key or value

dic={1:"Deepika", "age":35, "Degree":"B.tech"}
print(dic)
print(dic[1])
print(dic["age"])

# empty dictionary

 dict = {}
 dict["name"]= "Deepika"
 dict["age"]=25
 print(dict)