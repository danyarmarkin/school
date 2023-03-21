s = open("f5.txt", "r").readline()
a = s.split("C")[1:-1]
w = "234???57???8"
q = "0123456789"
r = []

for i in a:
    if len(i) != len(w):
        continue
    r.append(0)
    for j, l in enumerate(i):
        if w[j] == l or (l in q and w[j] == "?"):
            r[-1] = r[-1] * 10 + int(l)
p = 1
b = max(r)
c = "13579"
for i in range(1, len(str(b))):
    if str(b)[i] in c:
        p *= int(str(b)[i])
print(p)

