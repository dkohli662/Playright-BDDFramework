
file=open('text.txt')
#print(file.read())
#print(file.read(4))

# print(file.readline())
# print(file.readline())

# print all content of file line by line using readline()

""""
line=file.readline()
while line!="":
    print(line)
    line=file.readline()
   """
## same can be done using for loop -read data line by line
for list in file.readlines():
    print(list)

file.close()
