a = 0
b = 1
c = 0
win = []
fin = []

with open("codeab.txt", "r") as text:
    lines = [line.rstrip("\n") for line in text]
x = lines.pop(0)
x = int(x)
d = len(lines) - 1
try:
    while c <= d:
        a = 0
        b = 1
        z = lines.pop(0)
        while a <= len(z) - 2:
            if z[a] == "R" and z[b] == "S" or z[a] == "P" and z[b] == "S" or z[a] == "S" and z[b] == "P":
                win.append(1)
            elif z[a] == z[b]:
                pass
            else:
                win.append(2)
            a = a + 3
            b = b + 3
                
        fin.append(round(sum(win)/ len(win)))
        win = []
        
except:
    fin = " ".join(str(v) for v in fin)
    print(fin)
