from itertools import *
a = "МТР"
b = "ЕО"
comb = product(a + b, repeat=4)
k = 0
for i in comb:
    if i[0] in a and i[-1] in b:
        k += 1

print(k)