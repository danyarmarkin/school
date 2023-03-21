import math


def div_abs(n):
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            k = n // i
            return k - i
    return 0


r = 0
i = 350000
while r < 6:
    m = div_abs(i)
    if m % 23 == 9:
        print(i, m)
        r += 1
    i += 1
