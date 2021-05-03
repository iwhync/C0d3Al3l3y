# not very happy with this one, come back to it and fix it so it doesn't look like crap

import re
x = input("Input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
a = x.pop(0)
count = 2 # starts on 2 to include first and last passthrough
count2 = 0
y = 0
z = 1
while x != range(1,a): # literally does nothing except keep the loop running, don't know what i was thinking
    if z >= a:
        count += 1
        y = 0
        z = 1
    if x[y] > x[z]:
        x[y], x[z] = x[z], x[y]
        count2 += 1
    if sorted(x) == x:
        print(count,count2)
        break # fix this so when it's done, it's done. Force stop like this is awful.
    y += 1
    z += 1
