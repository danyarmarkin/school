import math


def comp(s):
    l = len(s)
    for i in range(l):
        for j in range(i + 1, l):
            r = ""
            for k in range(l):
                if k == i:
                    r += s[j]
                elif k == j:
                    r += s[i]
                else:
                    r += s[k]
            yield r


def simp(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


r = 0
i = 1411111113
simple = []
not_simple = []

while r < 5:
    if "0" not in str(i):
        if i not in simple:
            if simp(i):
                simple.append(i)
            else:
                i += 2
                continue
        m = 0
        s = set()
        for j in comp(str(i)):
            k = int(j)
            if k == i:
                continue
            if k in not_simple:
                continue
            elif k in simple:
                m = max(m, k)
                s.add(k)
            elif simp(k):
                m = max(m, k)
                s.add(k)
                simple.append(k)
            else:
                not_simple.append(k)

            if len(s) >= 12:
                print(i, m)
                r += 1
                break
        i += 2
    else:
        i += 10
