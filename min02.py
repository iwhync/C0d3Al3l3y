import re
x = input("input: ")
x = re.findall(r"[0-9.-]+",x)
x = [int(x) for x in x]
z = x.pop(0)
for num in range(z):
    a = x.pop(0)
    b = x.pop(0)
    if a > b:
        print(b)
    else:
        print(a)
