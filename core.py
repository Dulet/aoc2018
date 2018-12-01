f = open("input.txt", 'r')
array = f.readlines()
dab = []
for line in array:
    dab.append(line)

for a in range(0, len(dab)):
    dab[a] = dab[a][:-1]

resultarray = [0]
result = 0
s = set(resultarray)
value = 0
yay = 0
def loop(result, value = value, yay = yay):
    for a in range(0, len(dab)):
        if "+" in dab[a]:
            la = dab[a][1:]
            ma = int(float(la))
            result += ma
            if result in s:
                value += result
                yay += 1
                print(value)
                return str(value)
            if result not in s:
                s.add(result)

        elif "-" in dab[a]:
            al = dab[a][1:]
            wa = int(float(al))
            result -= wa
            if result in s:
                value += result
                yay += 1
                print(value)
                return str(value)
            if result not in s:
                s.add(result)
    return result

for f in range(0, 100000):
    if yay is 0:
        result = loop(result)
    else:
        print(value)
        break

