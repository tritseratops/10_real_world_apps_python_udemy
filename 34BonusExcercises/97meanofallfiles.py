import re
numbers=[]
path = '97meanofallfiles\\'
with open(path+'file2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        for m in re.finditer(r"\d+(\.\d+)?", line):
            numbers.append(float(str(m.group(0))))
with open(path+'file3.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        for m in re.finditer(r"\d+(\.\d+)?", line):
            numbers.append(float(str(m.group(0))))
sum_n=0
for number in numbers:
    sum_n=sum_n+float(number)
print(str((sum_n/len(numbers))))