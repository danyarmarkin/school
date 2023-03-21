f = lambda a, b, c=0: (1 if a == b else 0) if a >= b else f(a + 1, b, 1) + f(a + 2, b, 2) + f(a * 2, b, 3) * int(c != 3)
print(f(1, 11))
