s = open("f8.txt", "r").readlines()
a = [chr(ord("A") + i) for i in range(26)]

k = 0
t = 0
for i in s:
    if i.count("R") >= 30:
        continue
    for b in a:
        d = [k for k in i.split(b)[1: -1] if len(k) > 0]
        t += len(d)
        k = max(list(map(len, d)) + [k])

print(k + 2, t)
