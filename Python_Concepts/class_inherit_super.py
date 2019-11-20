class Rectangle:
    def __init__(self, wd, len):
        self.wd = wd
        self.len = len

    def area(self):
        return self.wd * self.len

    def perimeter(self):
        return self.wd * 2 + self.len * 2


class Square(Rectangle):
    def __init__(self, side):
        # super(Square, self).__init__(side, side)
        pass

    def sq_area(self):
        return super().area()


sq = Square(4)
print(sq.area())
print(sq.sq_area())
print(sq.perimeter())

