a = int(input())
b = int(input())
t = int(input())

print(min((a - (t % a)) % a, (b - (t % b))) % b)
