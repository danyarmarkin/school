s = input().split()
print([(s[i], s[i + 1]) for i in range(0, len(s) - 1, 2)])
