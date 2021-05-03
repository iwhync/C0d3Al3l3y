import re
x = input("Input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
for _ in range(z):
    s = x.pop(0)
    a = x.pop(0)
    b = x.pop(0)
    l = float((s/(a+b))*a)
    print("%.13G" % l)
