for i in range(int(input())):
    n, x = map(int, input().split())
    h = sorted(list(map(int, input().split())))
    h1 = h[:len(h) // 2]
    h2 = h[len(h) // 2:]


    def sol():
        for i in range(len(h1)):
            if h2[i] - h1[i] < x:
                return "NO"
        return "YES"


    print(sol())
