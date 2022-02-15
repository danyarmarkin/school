n, m, k = map(int, input().split())
white = min(k - 1, m)
red = m // k
print((white + red) * n)