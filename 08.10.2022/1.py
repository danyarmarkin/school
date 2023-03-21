s = open("f1.txt", "r").readline()
m = 0
n = 0
a = "BCDFGHJKLMNPQRSTVWXZ"
b = "AEOIUY"
i = 0

while i < len(s):
    if s[i] in a and s[i + 1] in b:
        n += 1
        i += 1
        m = max(m, n)
    else:
        n = 0
    i += 1

print(m)