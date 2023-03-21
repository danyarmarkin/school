s = open("f4.txt", "r").readline()
a = list(s.split("A"))
l = 1 + len(a[0])
m = 0
p = ""

for v in a:
    if v == p and v != "":
        l += len(v) + 1
        m = max(m, l)
    else:
        l = 2 + len(v)
        p = v
print(m)