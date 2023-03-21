div = {2: [2], 3: [3], 4: [2], 5: [5], 6: [2, 3], 7: [7], 8: [2], 9: [3], 10: [2, 5], 11: [11], 12: [2, 3], 13: [13], 14: [2, 7]}
r = 0
i = 14
while r < 5:
    s = set()
    for j in range(2, i + 1):
        for k in div[j]:
            s.add(k)
    if len(s) % 2 == 1:
        r += 1
        print(i, len(s))
    i -= 1