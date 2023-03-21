from itertools import *
a = "ГОД"
b = "ГД"
comb = product(a, repeat=6)
k = 0
for i in comb:
    if i[0] in b and i[-1] in b:
        k += 1

print(k)