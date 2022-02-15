n = int(input())
wheel = list(map(int, input().split()))
a, b, k = map(int, input().split())

stop_a = a // k - int(a % k == 0)
stop_b = b // k - int(b % k == 0)

i = stop_a
max_win = 0
while i <= stop_b and i < stop_a + n:
    max_win = max([max_win, wheel[i % n], wheel[-(i % n)]])
    i += 1
print(max_win)
