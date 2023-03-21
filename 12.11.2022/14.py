import math


def simp(n):
    b = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            b = False
    return b


i = 9998
while i < 10 ** 7:
    s = str(i)
    if s[0] == "9" and simp(int(s[1:-1])):
        print(i, i // 9998)
    i += 9998
