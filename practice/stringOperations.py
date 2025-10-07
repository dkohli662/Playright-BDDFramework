from collections import Counter
from tkinter.font import names


class A:
    def NameCount(self):
        name=input("enter name")
        print("Name lenght is :", len(name))

    def vowelFirst(self):
        s="Deepika".lower()
        vowels="aeiou"
        v=""
        c=""
        for ch in s:
            if ch in vowels:
                v+=ch
            else:
                c+=ch
        print("updated name is :", v+c)

    def vowelCount(self):
        s="Deepika".lower()
        vowels="aeiou"
        count=0
        for ch in s:
            if ch in vowels:
                count=count+1
        print("Total vowels:", count)

    def CharacterCount(self):
        s2="Deepika".lower()
        freq={}
        for ch in s2:
            freq[ch]=freq.get(ch, 0)+1
        print("Letters count :", freq)

    def DuplicateCount(self):
        name = "DDeepikaid".lower()
        freq={}
        for ch in name:
            freq[ch]=freq.get(ch, 0)+1
        for ch, count in freq.items():
            if count>1:
                print(f"{ch} → {count}")

    def operation(self):
        s="Reyansh"
        for ch in s:
            print(ch) # will print all chars in separate line

    def operation2(self):
        s="Reyansh"
        for ch in s:
            print(ch, end=" ") # will print all chars in single line separated by space

    def operation3(self):
        s="Reyansh"
        for ch in s:
            print(ch, end=",") # will print all chars in single line separated by coma

    def Count(self):
        s="Elephant"
        count=Counter(s)
        print(count)

    def removeSpace(self):
        s = "Deepika kohli".lower()
        s1 = s.replace(" ", "")
        print(s1)




obj=A()

#obj.NameCount()
#obj.vowelFirst()
#obj.vowelCount()
#obj.LetterCount()
#obj.DuplicateCount()
#obj.operation()
#obj.operation2()
#obj.operation3()
obj.Count()