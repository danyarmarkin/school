# 13152_x 7x25_100

c = 0
for i in range(6, 100):
    a = 1 * i ** 4 + 3 * i ** 3 + 1 * i ** 2 + 5 * i + 2
    b = 7 * 100 ** 3 + i * 100 ** 2 + 2 * 100 + 5
    if (a + b) % 11 == 0:
        c += 1
print(c)  # 9
