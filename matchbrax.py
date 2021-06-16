fin = []
with open("codeab.txt", "r") as a_file:
    for line in a_file:
        line = (''.join([char for char in line if char in('(){}[]<>')]))
        fin.append(line)
fin.pop(0)
x = len(fin)
for bracket in fin:
    while a < int(x):
        fin[a] = fin[a].replace("{}","").replace("[]","").replace("()","").replace("<>","")
        a += 1
    a = 0
for line in range(len(fin)):
    if fin[line] == "":
        print("1")
    else:
        print("0")
