from itertools import *
a = "ЕГЭИНФ"
comb = product(a, repeat=6)
k = 0
for i in comb:
    s = ""
    for j in i:
        s += j
    if i[0] == "Е" and i[-1] in "ЭИ" and s.count("ФИ") > 1 and s.count("ЕГЭ") == 0:
        k += 1

print(k)