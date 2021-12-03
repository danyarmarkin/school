n = int(input())
p = dict()
for _ in range(n):
    a, b = input().split()
    p[a], p[b] = b, a
print(p[input()])
