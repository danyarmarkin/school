class Tree(list):
    sum = 0

    class Node:
        right = 0
        left = 0
        s = 0

        def __init__(self, left, right):
            self.left = left
            self.right = right

    def __init__(self, a):
        super().__init__()
        self.sum = self.tree(a, 0, len(a))

    def tree(self, array, left, right):
        n = self.Node(left, right)
        self.append(n)
        if left == right - 1:
            n.s = array[left]
        else:
            n.s = self.tree(array, left, int((left + right) / 2)) + self.tree(array, int((left + right) / 2), right)
        return n.s


a = [i for i in range(1, 17)]
t = Tree(a)
print(t.sum)
print(*[i.s for i in t])
t.add(2, 10)
print(*[i.s for i in t])
