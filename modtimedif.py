import re
x = input("Input: ")
x = re.findall(r"[0-9]+",x)
x = [int(x) for x in x]
a = x.pop(0)
for _ in range(a):
    day1 = x.pop(0) * 24 * 60 * 60
    hour1 = x.pop(0) * 60 * 60
    min1 = x.pop(0) * 60
    sec1 = x.pop(0)
    day2 = x.pop(0) * 24 * 60 * 60
    hour2 = x.pop(0) * 60 * 60
    min2 = x.pop(0) * 60
    sec2 = x.pop(0)
    end = (day2+hour2+min2+sec2) - (day1+hour1+min1+sec1)
    day = end // (24 * 3600)
    end = end % (24 * 3600)
    hour = end // 3600
    end %= 3600
    minutes = end // 60
    end %= 60
    seconds = end
    print(f"({day} {hour} {minutes} {seconds})")
