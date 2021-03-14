import re
x = input("Input: ")
x = re.findall(r"[^!.? ]+",x)
a = int(x.pop(0))
mul = int(x[2])
end = []
while int(a) > 0:
    while mul > 1:
        res = int(x[0]) + int(x[1]) * mul - int(x[1])
        end.append(res)
        mul = mul - 1
    end.append(int(x[0]))
    print(sum(end))
    end = []
    x.pop(0)
    x.pop(0)
    x.pop(0)
    try:
        mul = int(x[2])
    except:
        print("end")
    finally:
        a = a - 1
