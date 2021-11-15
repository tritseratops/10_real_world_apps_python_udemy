import re
path = '112requestions\\'
with open(path+'file2.txt', 'r') as f:
    lines = f.readlines()

questions = re.finditer(r"(^|\?|\.)[^?|^.]+\?", lines[0])
output=[]
for question in questions:
    str = question.group(0)
    if (str[0]=='.' or str[0]=='?'):
        str = str[2:]
    output.append(str)
print(output)
# num1 = int(str(num1.g