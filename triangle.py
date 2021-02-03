x = input("Input: ")
x = re.findall(r"[0-9.]+",x)
n = x.pop(0)
a = 0
b = 1
c = 2
fin = []
while a <= int(n)*3:
    for num in x:
        fin.append(int(num))
        a = a + 1
a = 0
while a < int(n)*3:
    if fin[a] + fin[b] > fin[c] and fin[b] + fin[c] > fin[a] and fin[a] + fin[c] > fin[b]:
        print("1")
    else:
        print("0")
    a = a + 3
    b = b + 3
    c = c + 3
