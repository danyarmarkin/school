import math

i = 1


def simp(n):
    b = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            b = False
    return b


while i <= 1048576:
    if i < 99994:
        i <<= 1
        continue
    a = [i - 5 + k for k in range(11)]
    for j in a:
        if 99999 <= j <= 1048571 and simp(j):
            print(j, i)
    i <<= 1
