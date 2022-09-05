class Point:
    z = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")

Point.z = 10

point = Point(1, 2)
print(point.z)
point.draw()

another = Point(3, 4)
print(another.z)
another.draw()

print(getattr(point, "z"))

print(hasattr(point, "w"))

setattr(point, "w", 12)

print(hasattr(point, "w"))

delattr(point, "w")

print(hasattr(point, "w"))

print(vars(point))

print(dir(point))
