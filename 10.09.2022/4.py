n = 81 ** 2017 + 9 ** 5223 - 81
s = ""
p = 9
while n > 0:
    s = str(n % p) + s
    n //= p
print(s.count("8"))  # 4032