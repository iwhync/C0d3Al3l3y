x = input("Numbers Please: ")
x = re.findall(r"[^!.? ]+",x)
d = int(x.pop(0))
a = 0
b = 1
z = 0
print(x)
try:
    while z <= d+1:
        x[a] = int(x[a])
        x[b] = int(x[b])
        res = x[a] / x[b]
        res = res + 0.01
        print(round(res))
        a = a + 2
        b = b + 2
        d = d + 1
except:
    pass
