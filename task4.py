# 4*. 7.1 реалізувати через in.
import math


class Point:

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            print('Values are not numeric!')

    def __le__(self, other):
        if isinstance(other, Circle):
            return bool(math.sqrt((self.x - other.x) ^ 2 + (self.y - other.y) ^ 2)) <= other.radius
        return 'it is trouble'


class Circle:

    def __init__(self, x, y, radius):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(radius, (int, float)):
            self.x = x
            self.y = y
            self.radius = radius
        else:
            print('Values are not numeric!')

    def contains(self, point):
        if (math.sqrt((self.x - point.x) ^ 2 + (self.y - point.y) ^ 2)) > self.radius:
            return False
        else:
            return True


p1 = Point(100, 300)
c1 = Circle(1, 2, 3)
print(c1)

# print(Point(1, 2) in Circle(1, 2, 10))
print(p1 in c1)
