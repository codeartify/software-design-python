from shapes.color import Color
from shapes.point import Point
from shapes.radius import Radius
from shapes.shape import Shape


class Circle(Shape):
    def __init__(self, x, y, r):
        self.center = Point(x, y)
        self.radius = Radius(r)
        self.color = Color(Color.GREEN)

    def count_contained_points(self, points):
        number_of_contained_points = 0
        for point in points.points:
            if self.contains(point):
                number_of_contained_points += 1
        return number_of_contained_points

    def contains(self, point):
        return self.center.distance_to(point) <= self.radius.value

    def move_to(self, x, y):
        self.center = Point(x, y)

    def resize(self, r):
        self.radius = Radius(r)

    def format(self):
        color = self.color
        return f'circle: {{\n\tcenter: {self.center.format()} \n\tradius: {self.radius.format()} \n\tcolor: {color.color_as_text} \n}}'
