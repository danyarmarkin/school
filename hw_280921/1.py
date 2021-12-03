def gcd(a, b):  # 1
    if b == 0:
        return a
    return gcd(b, a % b)


def num(a, s):  # 2
    if a == 0:
        return s
    return num(a // 10, s + 1)

def summ(a, s):  # 3
    if a == 0:
        return s
    return summ(a // 10, s + (a % 10))

a = int(input())
b = int(input())
print(gcd(a, b))

a = int(input())
print(num(a, 0))
print(summ(a, 0))
