import re
x = input("Input: ")
x = re.findall(r"[0-9-]+",x)
x = [int(x) for x in x]
x.pop()
cou = 0
res = 0
y,z = 0,1
for _ in range(len(x)-1):
    if x[y] > x[z]:
        cou += 1
        x[y], x[z] = x[z], x[y]
    y += 1
    z += 1 
for num in x:
    res += num
    res *= 113
    res %= 10000007
print(cou,res)
