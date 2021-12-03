p = eval(input())
unzip = [[] for _ in range(len(p[0]))]
for i in p:
    for j in range(len(i)):
        unzip[j].append(i[j])
print([tuple(i) for i in unzip])