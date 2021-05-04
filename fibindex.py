import re
le = 1000
x,y = 0,1
it = 0
end = []
while it < le:
    end.append(x)
    z = x + y
    x = y
    y = z
    it += 1
x = input("Input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
a = 0
for _ in range(z):
    print(end.index(x[a]))
    a += 1
