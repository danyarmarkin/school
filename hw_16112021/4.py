p = dict()
for i in range(int(input())):
    a = input().split()
    for word in a:
        p[word] = p.get(word, 0) + 1

m = max(p.values())
w = [k for k, v in p.items() if v == m]
print(min(w))
