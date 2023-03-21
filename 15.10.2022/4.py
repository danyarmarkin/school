s = list(map(str.split, open("f4.txt", "r").readlines()))[1:]
a = [(int(i[0]), int(i[1]), i[2]) for i in s]
d = [["-" for _ in range(10000)] for _ in range(10000)]
for i in a:
    d[i[0] - 1][i[1] - 1] = i[2]
m = [0, 0]
for i, v in enumerate(d):
    def st(h):
        l = ""
        for j in h:
            l += j
        return l
    n = max(list(map(len, st(v).split("-"))))
    m = max(m, [n, i + 1])
print(*m)