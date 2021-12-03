s = input()
a = 0
r = 0
for i in s:
    if i == "(":
        a += 1
    else:
        if a == 0:
            r += 1
        else:
            a -= 1
print(a + r)