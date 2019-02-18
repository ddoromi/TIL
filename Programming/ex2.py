class Point:
    def __init__(self, x, y):
        self. x = x
        self. y = y

class Circle(Point):
    def __init__(self, Point, r):
        super().__init__(Point.x, Point.y)
        self.r = r
    def get_area(self):
        return self.r * self.r * 3.14
    
    def get_perimeter(self):
        return 2 * self.r * 3.14

    def get_center(self):
        return self.x, self.y

    def print(self):
        print(f'Circle: {self.x, self.y}, r: {self.r}')

p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()

p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()