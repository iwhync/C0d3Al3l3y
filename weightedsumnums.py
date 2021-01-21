def number():
    a = 1
    z = str(x.pop(a))
    q = len(z)
    b = 0
    result = []
    while int(q) > 0:
        for num in z:
            res = int(z[b]) * int(a)
            result.append(res)
            a = a + 1
            b = b + 1
            q = q - 1
        print(sum(result))

x = input("Post those numbers: ")
x = re.findall(r"[0-9.]+",x)
c = int(len(x)) - 1
for _ in range(c):
    number()
