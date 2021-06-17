import re
import math
x = input("Input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
l = x.pop(0)
i = x.pop(0)/100/12
n = x.pop(0)
m = math.ceil(l*((i*((1+i)**n))/((1+i)**n-1)))
print(m)
