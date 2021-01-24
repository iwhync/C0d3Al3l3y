import re
x = input("Input: ")
x = re.findall(r"[^!.? ]+",x)
z = int(x.pop(0))
a = 0
b = 1
fin = []
while int(z) > 0:
    if int(x[a]) > 0:
        le = len(x[b])
        num = int(x[a])
        fin.append(x[b][num:le]+x[b][0:num])
        a = a + 2
        b = b + 2
        z = z - 1
    if int(x[a]) < 0:
        num = int(x[a])
        fin.append(x[b][num:le]+x[b][0:num])
        a = a + 2
        b = b + 2
        z = z - 1        
fin = " ".join(str(v) for v in fin)
print(fin)
