s = input()
s1 = ""
s2 = ""
m = 0

for i in s:
    s1 += chr(ord(i) - 3)
    s2 += chr(ord(i) + 3)
    m += ord(i)

print(m)
print(s1)
print(s2)
