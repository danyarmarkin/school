from functools import reduce

print(reduce(lambda x, y: x * y, list(filter(lambda x: x < 0, list(map(int, input().split()))))))
