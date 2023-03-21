#  ZaYX_55 2XaY_55

a1 = 0
a2 = 0

for i in range(44):
    a = 35 * 55 ** 3 + i * 55 ** 2 + 34 * 55 + 33
    b = 2 * 55 ** 3 + 33 * 55 ** 2 + i * 55 + 34

    if (a - b) % 29 == 0:
        if a1 == 0:
            a1 = a - b
        a2 = a - b

print(abs(a1 - a2))