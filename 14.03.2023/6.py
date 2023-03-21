def tre(n):
    s = 0
    while n != 0:
        s += n % 3
        n //= 3
    return s


f = open("17-6.txt", "r")
a = [int(i[:-1]) for i in f.readlines()]

d = 0
h = 10000000
for i in a:
    if i > d and i % 11 == 0:
        d = i
    if i < h and i % 11 == 0:
        h = i

m = tre(d)
g = tre(h)

c1 = 0
c2 = 1000000000
for i in range(len(a) - 1):
    if tre(a[i]) == m or tre(a[i + 1]) == m:
        c1 += 1
        c2 = min(c2, a[i] + a[i + 1])

print("max =", c1)
print("min =", c2)
