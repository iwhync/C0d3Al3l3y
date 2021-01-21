x = input("String you want to reverse: ")
a = len(x)
print(a)
reverse = []
a = a - 1
while a > -1:
    reverse.append(x[a])
    a = a - 1
reverse = ''.join(str(v) for v in reverse)
print(reverse)
