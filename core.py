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
            if result in resultarray:
                print("AAAAAAAAA")
                value += result
                yay += 1
                return "DINGDINGDING: " + str(result)
            if result not in s:
                resultarray.append(result)

        elif "-" in dab[a]:
            al = dab[a][1:]
            wa = int(float(al))
            print(wa)
            print(result)
            result -= wa
            if result in resultarray:
                print("AAAAAAA")
                value += result
                yay += 1
                return "DINGDINGDING: " + str(result)
            if result not in s:
                resultarray.append(result)
    return result

for f in range(0, 100000):
    result = loop(result)
    print(value)
    if yay is not 0:
        break