# Implements Shape, Circle, and Rectangle classes using polymorphism, then stores them in a mixed list to calculate and print individual and total areas.

import math


class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")

    def __repr__(self):
        return f"{type(self).__name__} - Area: {self.area()}"


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


def main():
    c1, c2 = Circle(2), Circle(4)
    r1, r2 = Rectangle(2, 3), Rectangle(4, 5)

    shapes = [c1, c2, r1, r2]

    total_area = 0

    for shape in shapes:
        print(shape)
        total_area += shape.area()

    print(f"Total Area: {total_area}")


if __name__ == "__main__":
    main()