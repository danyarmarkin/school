for i in range(int(input())):
    n = int(input())
    s = input()
    d = [0] * 26
    for j in s:
        if d[ord(j) - ord("A")] == 0:
            d[ord(j) - ord("A")] += 2
        else:
            d[ord(j) - ord("A")] += 1
    print(sum(d))

