x = input("Nums: ")
x = re.findall(r"[0-9.]+",x)
z = int(x.pop(0))
q = len(x)
res = []
a = 0
b = 1
c = 2
while q >= 1:
    sm = int(x[a]),int(x[b]),int(x[c])
    sm = sorted(sm)
    res.append(sm[1])
    q = q - 3
    a = a + 3
    b = b + 3
    c = c + 3
res = ' '.join(str(v) for v in res)
print(res)
