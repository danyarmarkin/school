import math


def firstMoreSecond(n):
    return int(str(n)[0]) > int(str(n)[-1])


def isSimp(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


a = []
for i in range(2095, 10000):
    if firstMoreSecond(i) and isSimp(i):
        a.append(i)

print(len(a))

for i in a[::-1]:
    if i % 100 == 21:
        print(i)
        break
