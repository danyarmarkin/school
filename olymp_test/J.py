a, b, c, d = map(int, input().split())

sm = a * b
sp = c * d

if sm > sp:
    print("M")
elif sm < sp:
    print("P")
else:
    print("E")