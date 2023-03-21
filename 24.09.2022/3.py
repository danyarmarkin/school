a = list(map(int, open("f1.txt", "r").readlines()))
s = 0
m = 10 ** 10

for i in a:
    if i % 3 == i % 5 and (i % 53 == 0 or i % 47 == 0 or i % 31 == 0):
        m = min(m, i)
        s += 1

print(s, m)
