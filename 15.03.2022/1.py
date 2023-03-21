s, f = map(int, input().split())
a = [0] * (f - s + 1)

for i in range(f - s + 1):
    if i == 0:
        a[i] = 1
    if i == 1: