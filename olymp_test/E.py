a, b, c, d = map(int, input().split())

s1 = a * b + c * d
s2 = a * c + b * d
s3 = a * d + b * c

print(max(s1, s2, s3))