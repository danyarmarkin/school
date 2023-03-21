# task 9

import math


def calc_s(n):
    if n <= 2:
        return 0
    s = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s += i
            if (n // i) != i:
                s += n // i
    return s


a = []
i = 150000
while len(a) < 7:
    s = calc_s(i)
    if s % 13 == 10:
        a.append([i, s])
    i += 1
for j in a:
    print(*j)

