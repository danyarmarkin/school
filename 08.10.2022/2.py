s = open("f2.txt", "r").readline()
m = 0
n = 0
a = "ABC"
b = "123"
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