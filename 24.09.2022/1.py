from functools import reduce

a = 0
s = 0
for i in range(12345, 67891):
    if sum([int(k) for k in str(oct(i)[2:])]) == 19 and\
            reduce(lambda x, y: x * y, [int(k) for k in str(oct(i)[2:])]) % 5 == 0:
        if a == 0:
            a = i
        s += 1
print(s, a)