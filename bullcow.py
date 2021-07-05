import re
x = input("input: ")
x = re.findall(r"[0-9.]+",x)
y = x.pop(0)
z = x.pop(0)
a = 0
ybroke = []
ybroke.append(y[0])
ybroke.append(y[1])
ybroke.append(y[2])
ybroke.append(y[3])
end = []
end1 = []

for num in range(int(z)):
    for zum in str(x[num]):
        if str(zum) in str(y):
            end.append(1)
    while a < 4:
        for zum in str(x[num]):
            if str(zum) == ybroke[a]:
                end1.append(1)
            a += 1
    print(f"{sum(end1)}-{sum(end)-sum(end1)}")
    end = []
    end1 = []
    a = 0
