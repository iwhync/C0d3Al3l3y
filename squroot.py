import re
x = input("input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
for num in range(z):
    r = 1
    X = x.pop(0)
    n = x.pop(0)
    while n >= 0:
        r = (r+X/r) / 2
        n -= 1
        if n == 0:
            print(r)
