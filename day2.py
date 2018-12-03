""" part 1 """

f = open("input/day2.txt", "r")
read = f.readlines()

for a in range(len(read)):
    read[a] = read[a][:-1]

two = 0
three = 0


def count(string):
    # counts how often each letter appears in a string
    lib = {}
    for a in range(len(string)):
        if string[a] not in lib:
            lib[string[a]] = 1
        elif string[a] in lib:
            lib[string[a]] += 1
    return lib


def double(string):
    # searches which letters appeared twice
    global two
    a = count(string)
    for k,v in a.items():
        if a[k] == 2:
            two += 1
            break


def triple(string):
    # same as above, but for 3 elements
    global three
    a = count(string)
    for k,v in a.items():
        if a[k] == 3:
            three += 1
            break


for a in (range(len(read))):
    double(read[a])
    triple(read[a])

sum = two*three
print("Sum:", sum)

""" part 2 """


def first_difference(str1, str2):
    # finds which letters are different in two strings
    f = -1
    for a, b in zip(str1, str2):
        f += 1
        if a != b:
            str1 = str1[:f] + str1[(f+1):] + "1"  # adds indicator how many letters are different
            str2 = str2[:f] + str2[(f+1):] + "1"
            f = 0
    if str1.count("1") == 1: # if indicator happens once, we return that string
        str1 = str1.replace("1", "")
        return str1


for a in range(len(read)):
    for b in range(len(read)):
        ans = first_difference(read[a], read[b])
        if ans is not None:
            print(ans)
            break

