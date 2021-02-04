result = 0
final = []
x = input("Input: ")
x = re.findall(r"[0-9.]+",x)
n = x.pop(0)
a = 0
seed = 113
while a < int(n):
    result = (result + int(x[a])) * seed
    if result > 10000007:
        result = result % 10000007
    a = a + 1
print(result)
    
