import re
a = input("input: ")
x = re.findall(r"[0-9]+",a)
x = [int(x) for x in x]
y = re.findall(r"[+,*,%]+",a)
b = len(x)
c = len(y)
end = []
end2 = []
end3 = []
for num in range(c):
    end.append(x[num])
    end.append(y[num])
end.append(x[-1])
z = 0
z2 = len(end)
while z <= 1:
    if end[z] == "+":
        end2.append(end[z-1]+end[z+1])
        z += 1
    else:
        z += 1
while z != z2 and z > 1:
    if end[z] == "+":
        end2.append(sum(end2)+end[z+1])
        end2.pop(0)
        z += 1
    if end[z] == "*":
        end2.append(sum(end2)*end[z+1])
        end2.pop(0)
        z += 1
    else:
        z += 1
print(end2[0]%end[-1])
