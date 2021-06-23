import re
x = input("input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
z = x.pop(0)
end = []
endset = []
for num in range(z):
    b = True
    a = x.pop(0)
    while b == True:
        a = int(a)*int(a)
        a = str(a).zfill(8)
        a = a[2:6]
        end.append(a)
        if len(end) > 500:
            endset = set(end)
            print(len(endset)+1)
            end = []
            endset = []
            b = False
