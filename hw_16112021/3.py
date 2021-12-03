p = dict()
for _ in range(int(input())):
    a, b = input().split()
    p[a] = p.get(a, 0) + int(b)

for a, b in sorted(p.items()):
    print(a, b)
