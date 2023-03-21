s = open("f6.txt", "r").readlines()

k = 0
for i in s:
    d = list(map(int, i.split(".")))
    if d[-1] == 14 and len(d) == 4 and str(d[1])[0] == "2" and d[0] == 195:
        k += 1

print(k)
