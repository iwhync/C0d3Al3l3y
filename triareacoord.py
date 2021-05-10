x = input("input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
end = []
end2 = []
for num in range(z):
    x1 = x.pop(0)
    y1 = x.pop(0)
    x2 = x.pop(0)
    y2 = x.pop(0)
    x3 = x.pop(0)
    y3 = x.pop(0)
    end.append(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    print(abs(end[num]))
