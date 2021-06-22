import re
x = input("input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
for num in range(z):
    A = x.pop(0)
    C = x.pop(0)
    M = x.pop(0)
    X0 = x.pop(0)
    N = x.pop(0)
    n = N
    Xnext = X0
    for num in range(N):
        Xnext = (A * Xnext + C) % M
    print(Xnext)
