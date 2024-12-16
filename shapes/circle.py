from shapes.color import Color
from shapes.point import Point
from shapes.radius import Radius
from shapes.shape import Shape


def validate_coordinates(x_coords, y_coords):
    if is_empty(x_coords):
        raise ValueError("x coordinates are empty")
    if is_empty(y_coords):
        raise ValueError("y coordinates are empty")
    if differ_in_length(x_coords, y_coords):
        raise ValueError("Not every provided x coordinate has a matching y coordinate")


def differ_in_length(x_coords, y_coords):
    return len(x_coords) != len(y_coords)


def is_empty(coords):
    return coords is None or len(coords) == 0


class Circle(Shape):
    def __init__(self, x, y, r):
        self.center = Point(x, y)
        self.radius = Radius(r)
        self.color = Color(Color.GREEN)

    def count_contained_points(self, x_coords, y_coords):
        validate_coordinates(x_coords, y_coords)
        return self.count_points_within_circle(x_coords, y_coords)

    def count_points_within_circle(self, x_coords, y_coords):
        number_of_contained_points = 0
        points = []
        for i in range(len(x_coords)):
            point = Point(x_coords[i], y_coords[i])
            points.append(point)

        for point in points:
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
        return f'circle: {{\n\tcenter: {self.center.format()} \n\tradius: {self.radius.format()} \n\tcolor: {self.color.get_color_formatted(False)} \n}}'
