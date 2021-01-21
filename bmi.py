x = input("Post 'em: ")
x = re.findall(r"[0-9.]+",x)
d = int(x.pop(0))
a = 0
b = 1
z = 0
results = []
finish = []
try:
    while d != z:
        BMI = float(x[a]) / float(x[b]) **2    
        if BMI < 18.5:
            finish.append("under")
        if BMI > 18.5 and BMI < 25.0:
            finish.append("normal")
        if BMI > 25.0 and BMI < 30.0:
            finish.append("over")
        if BMI > 30.0:
            finish.append("obese")
        a = a + 2
        b = b + 2
        z = z + 1
except:
    pass

finish = ' '.join(str(v) for v in finish)
print(finish)
