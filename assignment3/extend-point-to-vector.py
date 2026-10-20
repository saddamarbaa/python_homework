
# Task 5: Extending Point to Vector

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
        )


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
            self.x + other.x,
            self.y + other.y
        )


# Task 5: Test Point and Vector
p1 = Point(1, 2)
p2 = Point(4, 6)

print(p1)
print(p2)
print("Points equal:", p1 == p2)
print("Distance:", p1.distance(p2))

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1)
print(v2)

v3 = v1 + v2
print("Vector sum:", v3)
print("Vectors equal:", v1 == v2)
print("Distance between vectors:", v1.distance(v2))
