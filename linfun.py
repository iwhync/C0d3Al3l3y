import re
x = input("input: ")
x = re.findall(r"[0-9.-]+",x)
x = [int(x) for x in x]
z = x.pop(0)
for num in range(z):
    a = x.pop(0)
    b = x.pop(0)
    c = x.pop(0)
    d = x.pop(0)
    e = int((d-b)/(c-a))
    f = int((b-e*a))
    print(f"({e} {f})")
