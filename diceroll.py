import re
x = input("input: ")
x = re.findall(r"[0-9.]+",x)
z = x.pop(0)
a = 0
end = []
while a < int(z):
    res = float(x[a]) * 6 + 1
    res = res // 1
    a = a + 1
    print(int(res))
