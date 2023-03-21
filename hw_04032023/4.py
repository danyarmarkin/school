from random import randint


class Node:
    def __init__(self, value, head):
        self.value = value
        self.head = head


class LinkedList:
    def __init__(self):
        self.currentNode = None

    def append(self, item):
        self.currentNode = Node(item, self.currentNode)

    def __len__(self) -> int:
        i = 0
        node = self.currentNode
        while node is not None:
            node = node.head
            i += 1
        return i

    def get_list(self) -> list:
        r = []
        node = self.currentNode
        while node is not None:
            r.append(node.value)
            node = node.head
        return r[::-1]

    def search(self, value):
        node = self.currentNode
        while node is not None:
            if node.value == value:
                return node
            node = node.head
        return None

    def remove_node(self, n):
        node = self.currentNode
        pre = None
        while node is not None:
            if node == n:
                if pre is None:
                    self.currentNode = node.head
                else:
                    pre.head = node.head
                return
            pre = node
            node = node.head


track = LinkedList()

for _ in range(25):
    track.append(randint(1, 25))
print(track.get_list())

m = max(track.get_list())
print(f"max element equals {m}")

while m in track.get_list():
    n = track.search(m)
    track.remove_node(n)
track.append(m)
print(track.get_list())