from itertools import *
a = "0123456"
comb = product(a, repeat=4)
k = 0
for i in comb:
    s = [i[0] + i[1], i[1] + i[2], i[2] + i[3]]

    if i[-1] in "0246" and s.count("56") + s.count("65") == 1:
        k += 1
print(k)