s = open("f3.txt", "r").readline()
x = 0
y = 0
m = 0

for i in s:
    if i == "0" and y == 0:
        x += 1
    elif i == "1" and x > 0:
        y += 1
        m = max(m, x + y)
    else:
        y = 0
        x = 0
print(m)