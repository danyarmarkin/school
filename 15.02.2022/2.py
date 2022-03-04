s = open("f2.txt", "r").readlines()
n, k, m = map(int, s[0].split())
s = list(map(int, sorted(s[1:])[::-1]))
print(s, len(s))
print(s[min(m + k - 1, n - 1)], s[k - 1])
# for i in range(len(s)):
#     if s[i] == 917:
#         print(i + 1)