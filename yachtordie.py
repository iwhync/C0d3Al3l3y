x=input("input: ")
x = re.findall(r"[0-9.]+",x)
a = 0
b = 0
c = 5
win = []
z = x.pop(0)
while a < int(z):
    handset = set(x[b:c])
    hand = sorted(x[b:c])
    if len(handset) == 1:
        win.append("yacht")
    elif len(handset) == 2:
        if hand[0] == hand[1] and hand[0] == hand[2] and hand[0] == hand[3]:
            win.append("four")
        if hand[1] == hand[2] and hand[1] == hand[3] and hand[1] == hand[4]:
            win.append("four")
        else:
            win.append("full-house")
    elif len(handset) == 3:
        if hand[0] == hand[1] and hand[0] == hand[2] or hand[1] == hand[2] and hand[1] == hand[3] or hand[2] == hand[4]:
            win.append("three")
        else:
            win.append("two-pairs")
    elif len(handset) == 4:
        win.append("pair")
    elif len(handset) == 5:
        if hand[0] == "1" and hand[1] == "2" and hand[2] == "3" and hand[3] == "4" and hand[4] == "5":
            win.append("small-straight")
        elif hand[0] == "2" and hand[1] == "3" and hand[2] == "4" and hand[3] == "5" and hand[4] == "6":
            win.append("big-straight")
        else:
            win.append("none")
            
    b = b + 5
    c = c + 5
    a = a + 1
win = " ".join(str(v) for v in win)
print(win)
