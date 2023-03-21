from itertools import *
a = "01234567"
comb = product(a, repeat=4)
k = 0
for i in comb:
    if i[0] != "0" and int(i[-2] + i[-1]) % 4 == 0:
        k += 1
print(k)