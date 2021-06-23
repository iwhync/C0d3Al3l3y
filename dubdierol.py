import re
x = input("input: ")
x = re.findall(r"[0-9.]+",x)
x = [float(x) for x in x]
z = int(x.pop(0))
for num in range(z):
    a = x.pop(0)
    b = x.pop(0)
    end1 = (a % 6) + 1
    end2 = (b % 6) + 1
    print(int(end1+end2))
