f = open("input.txt", 'r')
array = f.readlines()
dab = []
for line in array:
    dab.append(line)

for a in range(0, len(dab)):
    dab[a] = dab[a][:-1]

result = 0
for a in range(0, len(dab)):
    if "+" in dab[a]:
        dab[a] = dab[a][1:]
        dab[a] = int(float(dab[a]))
        result += dab[a]

    elif "-" in dab[a]:
        dab[a] = dab[a][1:]
        dab[a] = int(float(dab[a]))
        result -= dab[a]

