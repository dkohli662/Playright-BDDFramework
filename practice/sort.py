
def sorting():
    list = [5, 3, 1, 0, 2]
    n=len(list)
    for i in range(n):
        for j in range(i+1, n):
            if list[i]>list[j]:
                temp=list[i] # temp=5
                list[i]=list[j] # i=3
                list[j] = temp # j=5

    print("final sorted array is :", list)


sorting()





