import re
x = input("Input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
a = x.pop(0)
end = []
for _ in range(a):
    one = x.pop(0)
    two = x.pop(0)
    if one > two:
        p = math.gcd(one, two)
        q = int((two * one) / p)
        print(f"({p} {q})")  
    elif two > one:
        p = math.gcd(two, one)
        q = int((one * two) / p)
        print(f"({p} {q})")
