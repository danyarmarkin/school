class Item(str):
    n = 0


def find(L, target):
    start = 0
    end = len(L) - 1

    while start <= end:
        middle = int((start + end) / 2)
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint


for _ in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        q = Item(input())
        s.append(q)

    s1 = s
    s = sorted(s)

    for i in range(1, len(s)):
        for j in range(1, len(s[i])):
            if find(s, s[i][:j]) is not None:
                if find(s, s[i][j:]) is not None:
                    s[i].n = 1
                    break

    r = ""
    for i in s1:
        r += str(i.n)
    print(r)
