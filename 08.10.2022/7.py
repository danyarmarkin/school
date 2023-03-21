s = open("f7.txt", "r").readline()

k = 0
p = ""
for v in s + "A":
    if v in "AEIOUY" and p.count(".") >= 6:
        k = max(k, len(p))
        p = ""
    elif v in "AEIOUY":
        p = ""
    else:
        p += v

print(k)