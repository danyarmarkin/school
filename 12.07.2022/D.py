for _ in range(int(input())):
    n = int(input())
    l = {i: [] for i in range(1, 9)}
    s = []
    r = ""
    for i in range(n):
        q = input()
        s.append(q)
        l[len(q)].append(q)

    for i in s:
        def sol():
            for j in range(1, len(i)):
                s1 = [k for k in l[j] if k[0] == i[0]]
                s2 = [k for k in l[len(i) - j] if k[-1] == i[-1]]
                for g in s1:
                    for h in s2:
                        if g + h == i:
                            return "1"
            return "0"
        r += sol()

    print(r)
