for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    z = False
    for i in a[:-1]:
        if i == 0 and z:
            s += 1
            continue
        if i > 0:
            z = True
            s += i
    print(s)

