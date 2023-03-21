x = "8x121"
y = "7x575"

for i in range(10):
    a = int(x.replace("x", str(i)), 13) - int(y.replace("x", str(i)), 13)
    if a % 19 == 0:
        print(a // 19)
        break

# 1464
