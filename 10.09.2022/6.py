x = "x1418"
y = "1x037"
z = "2x209"

d = "0123456789abcdefghijklmnopqrstuvwxyz"
for i in range(13):
    a = int(x.replace("x", d[i]), 13) + int(y.replace("x", d[i]), 14)
    b = int(z.replace("x", d[i]), 19)
    if a == b:
        print(b)
        break

# 323104