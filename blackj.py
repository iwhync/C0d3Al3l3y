black = []
a = 1
b = 0
with open("codeab.txt", "r") as a_file:
    for line in a_file:
        line = line.strip()
        line = line.replace("K","10").replace("Q","10").replace("J","10").replace("T","10").replace(" ","+").replace("A","11")
        black.append(line)
while a <= int(black[0]):
    if eval(black[a]) > 21:
        black[a] = black[a].replace("11","1")
        if eval(black[a]) > 21:
            print("Bust")
        else:
            print(eval(black[a]))
    else:
        print(eval(black[a]))
    a = a + 1
