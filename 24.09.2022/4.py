a = list(map(int, open("f2.txt", "r").readlines()))

s = 0
m = 0

for i in a:
    if bin(i)[-4:] == "1001" and i % 5 == 1 and (i // 5) % 5 == 1:
        m = max(m, i)
        s += i
print(s, m)
