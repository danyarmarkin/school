class Operation:
    PLUS = "+"
    MINUS = "-"
    MULTIPLE = "*"
    DIVISION = "/"
    LEFT_BRACKET = "("
    RIGHT_BRACKET = ")"
    NONE = "."


class Node:

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.operation = Operation.NONE


class Tree:
    def __init__(self, expression: str):
        s = []
        current = 0
        for i in expression.replace(" ", ""):
            if i.isdigit():
                current *= 10
                current += int(i)
                if len(s) == 0 or not str(s[-1]).isdigit():
                    s.append(current)
                s[-1] = current
            else:
                s.append(i)
                current = 0
        self.head = Node()
        self.sett(self.check_brackets(s), self.head)

    def check_brackets(self, s):
        c = 0
        f = False
        for ind, i in enumerate(s):
            if type(i) == str and i == "(":
                c += 1
                if ind == 0:
                    f = True
                continue
            if type(i) == str and i == ")":
                c -= 1
                if c == 0 and ind != len(s) - 1:
                    return s
                continue
        return s[1:-1] if f else s

    def sett(self, v, node: Node):
        if len(v) == 1:
            node.value = v[0]
            return
        # print(*v)
        left = []
        right = []

        for operation in [Operation.PLUS, Operation.MINUS, Operation.MULTIPLE, Operation.DIVISION]:
            stack = 0
            for i in range(len(v) - 1, -1, -1):
                if type(v[i]) == str and v[i] == "(":
                    stack += 1
                    continue
                if type(v[i]) == str and v[i] == ")":
                    stack -= 1
                    continue
                if type(v[i]) == str and v[i] == operation and stack == 0:
                    left = v[:i]
                    right = v[i + 1:]
                    node.operation = operation
                    break
            if len(left) > 0 and len(right) > 0:
                n1 = Node()
                n2 = Node()
                node.left = n1
                node.right = n2
                self.sett(self.check_brackets(left), n1)
                self.sett(self.check_brackets(right), n2)
                return

    def calculate(self, node):
        if node.operation == Operation.NONE:
            return node.value
        if node.operation == Operation.PLUS:
            return self.calculate(node.left) + self.calculate(node.right)
        if node.operation == Operation.MINUS:
            return self.calculate(node.left) - self.calculate(node.right)
        if node.operation == Operation.MULTIPLE:
            return self.calculate(node.left) * self.calculate(node.right)
        if node.operation == Operation.DIVISION:
            return self.calculate(node.left) / self.calculate(node.right)


def calc(expression):
    try:
        tree = Tree(expression)
        return tree.calculate(tree.head)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Unknown"


'''
    test   :    1 + (1 + (1 - 3) / 2) * 4 + 2 * (7 + 2 + 1) 
    answer :    21
    output :    21
'''
