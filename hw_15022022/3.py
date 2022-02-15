s = open("z3.txt", "r").readlines()
a, n = map(int, s[0].split())
m = 0
for i in sorted(list(map(int, s[1:]))):
    if m + i < a:
        m += i
    else:
        break
print(m, max(list(map(int, s[1:]))))
