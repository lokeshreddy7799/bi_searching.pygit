import math

class Shape:
    def area(self):
        pass  # Placeholder for method overriding

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

rectangle = Rectangle(5, 4)
circle = Circle(3)
triangle = Triangle(6, 2)


print("Area of Rectangle:", rectangle.area())  # Output: 20
print("Area of Circle:", circle.area())        # Output: ~28.27
print("Area of Triangle:", triangle.area())    # Output: 6.0


total = total_area([rectangle, circle, triangle])
print("Total area of all shapes:", total)  # Output: ~54.27
