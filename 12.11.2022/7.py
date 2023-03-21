import math

simp = []

n = 30000
a = [i for i in range(n)]
a[1] = 0
for i in range(2, n):
    j = i * 2
    while j < n:
        a[j] = 0
        j += i
    if a[i] != 0:
        simp.append(a[i])


i = 33333
while i <= 55555:
    s = 0
    sqrt = int(math.sqrt(i))
    for j in simp:
        if j >= sqrt:
            break
        if i % j == 0:
            s += j
    if s > 250 and i % s == 0: print(i, s)
    i += 1
