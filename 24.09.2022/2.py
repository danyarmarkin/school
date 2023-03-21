def f1(n):
    s = ""
    p = 5
    while n > 0:
        s = str(n % p) + s
        n //= p
    return s[-1] == "3"


def f2(n):
    s = ""
    p = 7
    while n > 0:
        s = str(n % p) + s
        n //= p
    return s.count("0") == 0


s = 0
a = 0

for i in range(3399, 225599):
    if f1(i) and f2(i):
        a = i
        s += 1

print(s, a)
