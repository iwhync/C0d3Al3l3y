import re
import math
x = input("input: ")
x = re.findall(r"[0-9.]+",x)
x = [float(x) for x in x]
z = int(x.pop(0))
for num in range(z):
    X = x.pop(0)
    Y = x.pop(0)
    N = x.pop(0)
    print1 = math.floor(Y*N/(X+Y))
    print2 = math.floor(X*N/(X+Y))
    fast = int(max((print1 + 1) * X, print2 * Y))
    slow = int(max(print1 * X, (print2 + 1) * Y))
    if fast > slow:
        print(slow)
    else:
        print(fast)
