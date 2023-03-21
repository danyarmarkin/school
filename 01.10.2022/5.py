from itertools import *
a = "ТРКНЩ"
b = "АИЕ"
comb1 = permutations(a, 3)
comb2 = permutations(b, 3)
print(len(list(comb1)) * len(list(comb2)))
