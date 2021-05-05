import re
x = input("Input: ")
x = re.findall(r"[0-9-]+",x)
x = [int(x) for x in x]
z = x.pop(0)
for _ in range(z):
    a = x.pop(0)
    b = x.pop(0)
    c = x.pop(0)
    if a**2 + b**2 == c**2:
        print("R")
    if a**2 + b**2 < c**2:
        print("O")
    else:
        print("A")
