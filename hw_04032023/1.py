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
print("list length: ", len(track))

for i in [15, 8.2, "Berlin", 15]:
    track.append(i)
    print("list length: ", len(track))
    print(*track.get_list(), sep="\n")
    # print()
