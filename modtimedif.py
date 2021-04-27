import re
x = input("Input: ")
x = re.findall(r"[^!.? ]+",x)
a = int(x.pop(0))
res = []
for _ in range(a):
    day1 = int(x.pop(0)) * 24 * 60 * 60
    hour1 = int(x.pop(0)) * 60 * 60
    min1 = int(x.pop(0)) * 60
    sec1 = int(x.pop(0))
    day2 = int(x.pop(0)) * 24 * 60 * 60
    hour2 = int(x.pop(0)) * 60 * 60
    min2 = int(x.pop(0)) * 60
    sec2 = int(x.pop(0))
    first = day1+hour1+min1+sec1
    second = day2+hour2+min2+sec2
    end = second - first
    day = end // (24 * 3600)
    end = end % (24 * 3600)
    hour = end // 3600
    end %= 3600
    minutes = end // 60
    end %= 60
    seconds = end
    print(f"({day} {hour} {minutes} {seconds})")
