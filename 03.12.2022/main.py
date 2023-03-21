class Matrix(list):
    """
    3x3 Matrix
    """

    def __init__(self, l):
        super().__init__(l)

    def size(self):
        return len(self), len(self[0])

    def determinant(self):
        return self[0][0] * self[1][1] * self[2][2] + \
               self[0][1] * self[1][2] * self[2][0] + \
               self[1][0] * self[2][1] * self[0][2] - \
               self[2][0] * self[1][1] * self[0][2] - \
               self[0][0] * self[2][1] * self[1][2] - \
               self[2][2] * self[0][1] * self[1][0]


def readMatrix():
    n = int(input("n (количество строк) = "))
    return Matrix([list(map(int, input().split())) for _ in range(n)])


def transpon(m: Matrix):
    k = Matrix([[0] * m.size()[0] for _ in range(m.size()[1])])
    for i in range(len(m)):
        for j in range(len(m[i])):
            k[j][i] = m[i][j]
    return k


m = readMatrix()
# print(m.determinant())
print(*transpon(m), sep="\n")
