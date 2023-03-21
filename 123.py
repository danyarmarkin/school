from random import randint

c = 0

black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_line = [i for i in range(3, 37, 3)]

for i in range(10 ** 5):
    c -= 50
    n = randint(0, 36)
    if n == 0:
        continue

    if n in black:
        c += 60
    if n in red_line:
        c += 60


print(c)

