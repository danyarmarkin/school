def haveNine(n):
    for i in str(n):
        if i == "9":
            return True
    return False


def second(n):
    sum = 0
    while n > 0:
        if n % 10 > 5:
            sum += n % 10
        n //= 10
    return sum % 3 == 0


a = []
for i in range(2848, 109500):
    if haveNine(i) and second(i):
        a.append(i)

print(len(a))

for i in a[::-1]:
    if str(i)[0] == "8":
        print(i)
        break
