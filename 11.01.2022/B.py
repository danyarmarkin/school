n, m, r = map(int, input().split())
a = [0] * (n - 1) + list(map(int, input().split())) + [0] * (n - 1)
start = n - 1
print(a)
for i in range(0, m):
    s = 0
    print(i - n + 1 + start, i + n + start - 1)
    for j in range(i - n + 1 + start, i + n + start):
        pos = start + i - abs(start + i - j)
        print("m0", start + i)
        print("pos", pos)
        s += a[j] * pos ** 2
    print(s % r)
