from itertools import *
a = "КРОТ"
comb = product(a, repeat=6)
k = 0
for i in comb:
    k += int(i.count("К") == 1)
print(k)
