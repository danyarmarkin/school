class Tree:
    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.t = [0] * 2 * size
        self.size = size

    def set_hard(self, i, v, x, lx, rx):
        if rx - lx == 1:
            self.t[x] = v
            return
        m = (lx + rx) // 2
        if i < m:
            self.set_hard(i, v, 2 * x + 1, lx, m)
        else:
            self.set_hard(i, v, 2 * x + 2, m, rx)
        self.t[x] = self.t[2 * x + 1] + self.t[2 * x + 2]

    def set(self, i, v):
        self.set_hard(i, v, 0, 0, self.size)

    def sum_hard(self, l, r, x, lx, rx) -> int:
        if lx >= r or rx <= l:
            return 0

        if lx >= l and rx <= r:
            return self.t[x]

        m = (lx + rx) // 2
        return self.sum_hard(l, r, x * 2 + 1, lx, m) + self.sum_hard(l, r, x * 2 + 2, m, rx)

    def sum(self, l, r):
        return self.sum_hard(l, r, 0, 0, self.size)


n, m = map(int, input().split())
a = list(map(int, input().split()))
t = Tree(n)
for i, v in enumerate(a):
    t.set(i, v)

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 1:
        t.set(a, b)
    else:
        print(t.sum(a, b))