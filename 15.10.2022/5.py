s = open("f5.txt", "r").readlines()[1:]
d = dict()
for i in s:
    a = i.split(".")
    l = a[0] + "." + a[1] + "." + str(int(a[2]) & 224) + ".0"
    d[l] = d.get(l, 0) + 1
m = 0
for k, v in d.items():
    m = max(m, v)
print(min([k for k, v in d.items() if len(v) == m]), m)