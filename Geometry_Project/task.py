from figures import *


class Task:
    dots = []
    segments = []
    distances = dict()

    def __init__(self, dots):
        self.dots = dots

    def prepareTriangles(self):
        print("start")
        triangles = []
        for i in self.dots:
            sides = dict()
            for j in self.dots:
                if i == j:
                    continue
                segment = Segment(i, j)
                if segment in self.segments:
                    continue
                self.segments.append(segment)
                length = segment.length()
                for dot, l in sides.items():
                    if l == length:
                        triangle = Triangle(dot, j, i)
                        if not triangle.isLine():
                            triangles.append(triangle)
                sides[j] = length
        print(*triangles)
        print("done")
        return triangles

    def getDots(self, triangles):
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
