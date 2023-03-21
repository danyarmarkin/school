s = list(map(str.split, open("f2.txt", "r").readlines()))
k = int(s[0][1])
a = sorted([[int(i[1]), int(i[2])] for i in s[1:] if i[0] == "A"], key=lambda x: x[0]) + [[0]]
while k - a[0][0] >= 0 and len(a) > 1:
    k -= a[0][0]
    a[0][1] -= 1
    a = a[int(a[0][1] == 0):]
z = sorted([[int(i[1]), int(i[2])] for i in s[1:] if i[0] == "Z"], key=lambda x: x[0])
p = 0
while k - z[0][0] >= 0 and len(z) > 1:
    k -= z[0][0]
    z[0][1] -= 1
    p += 1
    z = z[int(z[0][1] == 0):]
print(p, k)