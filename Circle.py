import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def compute_area(self):
        return round(math.pi * self.radius ** 2, 2)

    def compute_perimeter(self):
        return round(2 * self.radius * math.pi, 2)

c1 = Circle(10)
print(c1.compute_area())
print(c1.compute_perimeter())
