a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*sorted(set(a) & set(b)))
