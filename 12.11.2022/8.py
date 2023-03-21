import math


def div_sum(n):
    s = 0
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            k = n // i
            s += i + k
    if n == sqrt ** 2:
        s -= sqrt
    return s


r = 0
i = 150001
while r < 7:
    s = div_sum(i)
    if s % 13 == 10:
        print(i, s)
        r += 1
    i += 1