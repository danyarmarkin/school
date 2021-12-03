p = dict()
for _ in range(int(input())):
    c, *cs = input().split()
    for city in cs:
        p[city] = c

for _ in range(int(input())):
    print(p[input()])
