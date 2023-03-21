#  19x61_12 + 3393x_17 = 60x05_15

for i in range(10):
    a = int("19x61".replace("x", str(i)), 12)
    b = int("3393x".replace("x", str(i)), 17)
    c = int("60x05".replace("x", str(i)), 15)

    if a + b == c:
        print(c)
        break
