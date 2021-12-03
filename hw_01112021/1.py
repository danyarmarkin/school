p = eval(input())
sums = [0 for _ in range(len(p[0]))]
for i in p:
    for j in range(len(i)):
        sums[j] += i[j]
print(tuple(sums))
