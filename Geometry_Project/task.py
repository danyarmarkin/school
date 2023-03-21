from figures import *


# решение задачи
class Task:
    dots = []
    segments = []
    distances = dict()

    def __init__(self, dots):
        self.dots = dots

    def prepareTriangles(self):
        print("start")
        triangles = []
        for i in range(len(self.dots)):
            for j in range(i + 1, len(self.dots)):
                r = Segment(self.dots[i], self.dots[j]).length()

                def q(d: Dot):
                    return (d.x - self.dots[i].x) ** 2 + (d.y - self.dots[i].y) ** 2 == r

                for k in range(j + 1, len(self.dots)):
                    d1 = self.dots[i]
                    d2 = self.dots[j]
                    d3 = self.dots[k]
                    if q(self.dots[k]):
                        t = Triangle(d1, d2, d3)
                        if not t.isLine():
                            triangles.append(t)

        print(*triangles)
        print("done")
        return triangles

    @staticmethod
    def getDots(triangles):
        dots = {}
        for triangle in triangles:
            try:
                dots[triangle.dots[0]] += 1
            except KeyError:
                dots[triangle.dots[0]] = 1
            try:
                dots[triangle.dots[1]] += 1
            except KeyError:
                dots[triangle.dots[1]] = 1
            try:
                dots[triangle.dots[2]] += 1
            except KeyError:
                dots[triangle.dots[2]] = 1
        for dot, a in dots.items():
            print(dot, a)
        return dots
