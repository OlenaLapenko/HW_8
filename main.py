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


