s = open("f2.txt", "r").readlines()
n = map(int, s[0].split())
s = list(map(int, sorted(s[1:])))
d = sorted(list(filter(lambda x: x > 100, s)))
k = d[:int(len(d) / 2)]
sale = int(sum(k) * 0.9) + int(sum(k) % 1 != 0)
print(sum(s) - sum(d) + sale + sum(d[int(len(d) / 2):]))
print(max(k))

