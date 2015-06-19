__author__ = 'tracyrohlin'

class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = sorted([side1, side2, side3], reverse=True)

        if min(self.sides) <= 0:
            raise TriangleError
        smallest_side = self.sides[0] - self.sides[1]
        if self.sides[2] <= smallest_side:
            raise TriangleError

    def kind(self):
        edges = set(self.sides)
        if len(edges) == 1:
            return "equilateral"
        elif len(edges) == 2:
            return "isosceles"
        else:
            return "scalene"

class TriangleError(Exception):
    pass

