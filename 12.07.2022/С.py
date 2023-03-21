for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        s = input().split()[1]
        d = s.count("U") - s.count("D")
        a[i] = (a[i] - d) % 10
    print(*a)