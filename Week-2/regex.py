import re
file = open('sum.txt')
s = 0
for line in file:
    line = line.strip()
    x = re.findall('[0-9]+', line)
    if not x:
        continue
    else:
        for i in x:
            s = s + int(i)
print('The Sum is =', s)
