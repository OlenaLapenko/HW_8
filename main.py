# 1. Створити frange ітератор. Який буде працювати з float.


class Frange:
    def __init__(self, start, finish=None, step=None):
        self.start = start
        self.finish = finish
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.finish is None:
            self.finish = self.start + 0.0
            self.start = 0.0
        if self.step is None or self.step == 0:
            self.step = 1.0
        if self.step > 0 and self.start >= self.finish:
            raise StopIteration('ffff')
        elif self.step < 0 and self.start <= self.finish:
            raise StopIteration('ffff')
        if self.step > 0:
            if self.start + self.step - self.step > self.finish:
                raise StopIteration('ffff')
            result = self.start
            self.start += self.step
            return result
        if self.step < 0:
            if self.start + self.step - self.step < self.finish:
                raise StopIteration('ffff')
            result = self.start
            self.start += self.step
            return result


assert(list(Frange(5)) == [0, 1, 2, 3, 4])
assert(list(Frange(2, 5)) == [2, 3, 4])
assert(list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(Frange(1, 5)) == [1, 2, 3, 4])
assert(list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(Frange(0, 0)) == [])
assert(list(Frange(100, 0)) == [])


for i in Frange(1, 100, 3.5):
    print(i)


#2. Створити context manager який буде фарбувати колір виведеного тексту

class Colours:
    def __init__(self, colour):
        self.colour = colour

    def __enter__(self):
        return None

    def __exit__(self):
        return


#3. Реалізувати метод square в фігурах які залишилися. (Triangle+Parallelogram). Triangle - треба створити клас

class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 20, 30, 45)
p.x
p1 = Parallelogram(1, 2, 20, 30, 45)
str(p1)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)

scene.total_square()

#4*. 7.1 реалізувати через in.

Point(1, 2) in Circle(1, 2, 10) -> True or False
p1 in c1 -> True or False