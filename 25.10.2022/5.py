n = int(input())
d = []
for i in range(n):
    d.append([int(input())])
    d[-1].append(int(input()))

if n == 2:
    print(1)
    print(1, 2)
elif n == 3:
    d.sort(key=lambda x: x[0])
    print(3)

