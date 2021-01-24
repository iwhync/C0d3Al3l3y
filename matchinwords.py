x = input("Input: ")
x = x.split(" ")
end = []
uni = []
a = 0
for word in x:
    if x[a] not in end:
        end.append(x[a])
        a = a + 1
    else:
        uni.append(x[a])
        a = a + 1
uni = sorted(set(uni))
uni = " ".join(str(v) for v in uni)
print(uni)
