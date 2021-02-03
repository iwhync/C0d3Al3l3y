import re
ori = input("Input: ")
ori = re.findall(r"[0-9.]+",ori)
n = ori.pop(0)
fin = []
new = []
a = 0
while a <= int(n)-1:
    for num in ori:
        new.append(int(num))
        a = a + 1
ori = new
new = sorted(new)
a = 0
while a <= int(n)-1:
    index = ori.index(new[a])
    fin.append(index+1)
    a = a + 1
fin = " ".join(str(v) for v in fin)
print(fin)
