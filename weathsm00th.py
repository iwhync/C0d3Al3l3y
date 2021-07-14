import re
x = input("input: ")
x = re.findall(r"[0-9.]+",x)
x = [float(x) for x in x]
z = int(x.pop(0))
end = []
end.append(x[0])
a = 0
b = 1
c = 2
while c != z:
    num = (x[a]+x[b]+x[c])/3
    num = str(num)
    if len(end) == z-1:
        end.append(x[-1])
        a += 1
        b += 1
        c += 1
    else:
        num = float(num)
        end.append('%.12f'%num)
        a += 1
        b += 1
        c += 1
end = str(end)
end = "".join(end)
end = end.replace(",","").replace("[","").replace("]","").replace("'","").replace("00000000000","")
print(end,x[-1])
    
