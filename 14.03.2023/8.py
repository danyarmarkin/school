f = open("17-8.txt", "r")
a = [int(i[:-1]) for i in f.readlines()]

c = 0
m = 0
for i in range(len(a) - 6):
    q = a[i]
    w = a[i + 1]
    e = a[i + 2]
    r = a[i + 3]
    t = a[i + 4]
    y = a[i + 5]

    if e - w == w - q > 0 and y / t == t / r > 1 and e - w == y // t:
        c += 1
        m = max(m, q + w + e + r + t + y)
        continue

    if e / w == w / q > 1 and y - t == t - r > 0 and e // w == y - t:
        c += 1
        m = max(m, q + w + e + r + t + y)

print(c, m)
