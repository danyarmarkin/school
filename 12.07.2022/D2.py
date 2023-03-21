for _ in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    r = ""
    for i in s:
        r += "0"
        for j in range(1, len(i)):
            try:
                s.index(i[:j])
                s.index(i[j:])
                r = r[:-1]
                r += "1"
                break
            except ValueError:
                pass
    print(r)