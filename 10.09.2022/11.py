#  7∙512^3200 + 6∙256^3100 – 5∙64^3000 – 4∙8^2900 – 1542

n = 7 * 512 ** 3200 + 6 * 256 ** 3100 - 5 * 64 ** 3000 - 4 * 8 ** 2900 - 1542
s = 0
p = 64
while n > 0:
    s += str(n % p).count("0")
    n //= p
print(s)
