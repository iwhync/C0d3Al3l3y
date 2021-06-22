import re
x = input("input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
X0 = x.pop(0)
consonant = "bcdfghjklmnprstvwxz"
vowel = "aeiou"
word = []
A = 445
C = 700001
M = 2097152
xnext = X0
word = []
for num in range(z):
    length = x.pop(0)
    xnext = (A * xnext + C) % M
    x1 = xnext
    x1 = x1 % 19
    length -= 1
    word.append(consonant[x1])
    length -= 1
    while length >= 0:
        if len(word) % 2 != 0:
            xnext = (A * xnext + C) % M
            x1 = xnext
            x1 = x1 % 5
            length -= 1
            word.append(vowel[x1]) 
        else:
            xnext = (A * xnext + C) % M
            x1 = xnext
            x1 = x1 % 19
            length -= 1
            word.append(consonant[x1])  
    word = "".join(word)
    print(word)
    word = []
