n, k = map(int, input().split())
p = list(map(int, input().split()))
m = int((2 * n - k + 1) * k / 2)

if sum(p) >= m:
    print(-1)
    exit(0)

for i in range(k - 1, -1, -1):
    if p[i] < n - k + i + 1:
        p[i] += 1
        p = p[:i] + list(range(p[i], p[i] + k - i))
        break

print(*p)
