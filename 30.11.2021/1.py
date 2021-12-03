a = input().split()
s, sign = [i for i in a if i not in "+-"], [i for i in a if i in "+-"]

i = 0
while i < len(s):
    if str(s[i]) in "*//":
        s[i], s[i+1] = s[i+1], s[i]
        i += 1
    i += 1

for i in reversed(sign):
    s.append(i)
print(*s)
