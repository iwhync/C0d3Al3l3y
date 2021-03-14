import re
x = input("Input: ")
x = re.findall(r"[^!.? ]+",x)
a = int(x.pop(0))
b = 0
dic = []
che = []
end = []
with open("words.txt", "r") as a_file:
    for words in a_file:
        words = words.replace("\n","")
        words = sorted(words)
        words = "".join(words)
        dic.append(words)
    for word in x:
        word = sorted(word)
        word = "".join(word)
        che.append(word)
var = len(dic) - 1
while b < a:
    while var > 1:
        if dic[var] == che[b]:
            end.append(1)
            var = var - 1
        else:
            var = var - 1
    amm = len(end) - 1
    print(amm)
    end = []
    b = b + 1
    var = len(dic) - 1
