from itertools import *
a = sorted("СТЕПУХА")
comb = product(a, repeat=4)
k = 0
for i in list(comb)[1000:]:
    if i[0] != i[1] and i[1] != i[2] and i[2] != i[3]:
        k += 1
print(k)