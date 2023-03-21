import math


def div_sum(n):
    s = 0
    m = -1
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            k = n // i
            s += i + k
            m = max(m, k)
    if n == sqrt ** 2:
        s -= sqrt
    return s, m


r = 0
i = 520001

while r < 5:
    s, m = div_sum(i)
    if str(s) == str(s)[::-1] and m != -1:
        r += 1
        print(i, m)
    i += 1
