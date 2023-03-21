def tre(n):
    s = 0
    while n != 0:
        if n % 5 == 4:
            s += 4
        n //= 5
    return s


sm = 0

f = open("17-7.txt", "r")
a = [int(i[:-1]) for i in f.readlines()]


for i in a:
    if i % 12 == 0:
        sm += tre(i)

cnt = 0
mm = 0

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if x > sm and y > sm:
        cnt += 1
        mm = max(mm, x + y)

print(cnt, mm)
