import re
x = input("Input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
a = x.pop(0)
b = 0
end = 0

for _ in range(a):
    while x[b] != 1:
        if x[b] % 2 == 0:
            x[b] = int(x[b] / 2)
            end += 1
        else:
            x[b] = int(3 * x[b] + 1)
            end += 1
    if x[b] == 1:
        print(end)
        end = 0
        b += 1
