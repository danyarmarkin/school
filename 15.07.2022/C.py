for _ in range(int(input())):
    n, c, q = map(int, input().split())
    s = input()
    a = n
    d = [n]
    w = []

    for _ in range(c):
        l, r = map(int, input().split())
        a += r - l + 1
        d.append(a)
        w.append(l)

    for _ in range(q):
        k = int(input())
        i = len(d) - 1
        while k > n:
            if d[i] >= k > d[i - 1]:
                k -= d[i - 1]
                k += w[i - 1] - 1
            i -= 1
        print(s[k - 1])

