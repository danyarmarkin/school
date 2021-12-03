n, m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(int(input()))
for _ in range(m):
    b.add(int(input()))

print(len(a & b))
print(*sorted(a & b))

print(len(a - b))
print(*sorted(a - b))

print(len(b - a))
print(*sorted(b - a))
