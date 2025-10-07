s = "Deepika".lower()
vowels = "aeiou"
v = 0
c = 0
for ch in s:
    if ch in vowels:
        v = v + 1

    else:
        c = c + 1
print(v, c)