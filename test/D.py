def sol(s, t):
    def pr(n):
        return int(n * (n + 1) / 2)

    c = [-1]
    r = 0
    for i in range(len(s) - len(t) + 1):
        if s[i: i + len(t)] == t:
            r += pr(i + len(t) - c[-1] - 2)
            if len(c) > 1:
                r -= pr(max(0, len(t) - 2))
            # print(pr(i + len(t) - c[-1] - 2), pr(max(0, len(t) - 2)))
            c.append(i)

    r += pr(len(s) - c[-1] - 1)
    r -= pr(min(len(t) - 2, len(s) - c[-1] - 1))

    print(max(0, r))


for i in range(int(input())):
    s = input()
    t = input()
    sol(s, t)