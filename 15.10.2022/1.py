s = list(map(str.split, open("f1.txt", "r").readlines()))
n = sorted([(int(i[0]), int(i[1])) for i in s[1:]], key=lambda x: x[1] / x[0] * 10 ** 5 - x[0])[:int(s[0][1])]
print(sum([i[0] for i in n]), sorted(n, key=lambda x: x[0], reverse=True)[0][1])