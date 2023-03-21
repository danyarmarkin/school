t = int(input())
r = int(input())
l = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())
p = [p1, p2, p3]

c = l * r - t
s = c // sum(p) * 3
c %= sum(p)
if c > 0:
    s += 1
    c -= p1
if c > 0:
    s += 1
    c -= p2
if c > 0:
    s += 1
print(max(0, s))