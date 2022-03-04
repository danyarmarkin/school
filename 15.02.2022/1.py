s = open("f1.txt", "r").readlines()
n, m, k = map(int, s[0].split())
s = s[1:]
l = ["-" * n] * m

for i in s:
    x, y = map(int, i.split())
    l[x - 1] = l[x - 1][:y - 1] + "+" + l[x - 1][y:]

r = 0
m = 0
ind = 0
for h, line in enumerate(l):
    k = sum([i - 3 for i in [len(j) for j in line.split("+")] if i - 3 > 0])
    if k > m:
        ind = h
    m = max(k, m)
    r += k
print(r, ind + 1)
