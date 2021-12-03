p = [{input() for _ in range(int(input()))} for _ in range(int(input()))]
i = p[0]
u = p[0]
for j in p:
    i = i & j
    u = u | j
print(len(i))
print(*sorted(i))

print(len(u))
print(*sorted(u))
