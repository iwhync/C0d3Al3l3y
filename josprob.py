x = input("Input: ")
x = re.findall(r"[0-9-]+",x)
x = [int(x) for x in x]
pos = x.pop()-1
nums = []
for num in range(0,x[0]+1):
    nums.append(num)
idx = 0
len_list = (len(nums)-1)
while len_list>0:
    idx = (pos+idx)%len_list
    a = (nums.pop(idx))
    len_list -= 1
print(int(a) + 1)
