x = input("Input: ")
x = re.findall(r"[0-9.]+",x)
z = x.pop(0)
tally = []
for num in x:
    if num != "0":
        tally.append(int(num))
    if num == "0":
        a = len(tally)
        b = sum(tally)/a
        print(round(b))
        tally.clear()
