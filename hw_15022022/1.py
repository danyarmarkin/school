s = open("z1.txt", "r").readline()
r = ""
r1 = ""
for i in range(len(s)):
    if i == len(s) - 3:
        r1 += s[i] + s[i + 1] + s[i + 2]
        if len(r) < len(r1):
            r = r1
        break
    if s[i] + s[i + 1] + s[i + 2] + s[i + 3] == "XZZY":
        r1 += "XZZ"
        if len(r) < len(r1):
            r = r1
        r1 = ""
        continue
    r1 += s[i]
print(len(r))