n = int(input())
k = int(input())
p = [0 for _ in range(n)]
p[k % n] = 1
p[(k + 1) % n] = 1
i = k % n
while p[0] == 0:
    if p[i] == 0:
        i += 1
        i %= n
        continue
    if p[(i + k + 1) % n] == 0:
        p[(i + k + 1) % n] = p[i] + 1
    else:
        p[(i + k + 1) % n] = min(p[(i + k + 1) % n], p[i] + 1)
    if p[(i + k) % n] == 0:
        p[(i + k) % n] = p[i] + 1
    else:
        p[(i + k) % n] = min(p[(i + k) % n], p[i] + 1)
    i += 1
    i %= n
print(p[0])
