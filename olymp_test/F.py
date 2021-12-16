n = int(input())
d = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    j = 1
    while j * i <= n:
        d[i*j] += 1
        j += 1

print(d.index(max(d)))
print(max(d))
