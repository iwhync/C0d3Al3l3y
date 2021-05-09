import re
x = input("input")
x = re.findall(r"[0-9-]+",x)
x = [int(x) for x in x]
z = x.pop(0)
end = []
for num in range(z):
    a = bin(x[num] if x[num] > 0 else x[num] + (1<<32))
    end.append(a)
for num in range(z):
    print(end[num].count("1"))
