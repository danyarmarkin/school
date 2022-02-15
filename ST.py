a = list(map(int, input().split()))
n = len(a)
st = [0] * (n * 4)


def build(st, v, l, r):
    if l == r:
        st[v] = a[l]
    else:
        build(st, 2 * v + 1, l, (l + r) // 2)
        build(st, 2 * v + 2, (l + r) // 2 + 1, r)
        st[v] = st[2 * v + 1] + st[2 * v + 2]


def query(st, v, l, r, l1, r1):
    if l1 <= l and r <= r1:
        return st[v]
    if r < l1 or l > r1:
        return 0
    return query(st, 2 * v + 1, l, (l + r) // 2, l1, r1)\
           + query(st, 2 * v + 2, (l + r) // 2 + 1, r, l1, r1)


def add(st, v, l, r, ind, m):
    if l == r == ind:
        st[v] += m
        return m
    if r < ind or l > ind:
        return 0
    st[v] += add(st, 2 * v + 1, l, (l + r) // 2, ind, m) + add(st, 2 * v + 2, (l + r) // 2 + 1, r, ind, m)
    return 0


build(st, 0, 0, n - 1)
print(query(st, 0, 0, n - 1, 1, 5))
add(st, 0, 0, n - 1, 3, 12)
print(st)
print(query(st, 0, 0, n - 1, 1, 5))
