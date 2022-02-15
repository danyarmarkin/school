print(*filter(lambda x: int(x) % 5 == 0, input().split()))
print(*[i for i in input().split() if int(i) % 5 == 0])
