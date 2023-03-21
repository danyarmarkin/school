s = list(map(str.split, open("f3.txt", "r").readlines()))
k = int(s[0][1])
a = [(int(i[0]), int(i[1]), int(i[2])) for i in s[1:]]
d = dict()
for i in a:
    c = (i[1]) * 10 + i[0]
    if (c) not in d.keys():
        d[c] = [True] + [False for _ in range(k - 2)] + [True]
    d[c][i[2] - 1] = True
m = 0
p = 0
for i, v in d.items():
    g = [v[i: i + 4] for i in range(len(v) - 3)]
    if [False] * 4 in g:
        m = max(m, i)
        p += 1
print(m // 10, p)