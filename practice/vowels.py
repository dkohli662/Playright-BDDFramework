string = "Deepika"
vowels = "aeiouAEIOU"

v = ""
c = ""

for ch in string:
    if ch in vowels:
        v += ch
    else:
        c += ch

print("Result:", v+c)
