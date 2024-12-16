from shapes.color import Color
from shapes.shape import Shape


def square(value):
    return value * value


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


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Radius:
    def __init__(self, value):
        self.value = value


class Circle(Shape):
    def __init__(self, x, y, r):
        if r <= 0:
            raise ValueError("Radius needs to be larger 0")
        self.center = Point(x, y)
        self.radius = Radius(r)
        self.color = Color(Color.GREEN)

    def count_contained_points(self, x_coords, y_coords):
        validate_coordinates(x_coords, y_coords)
        return self.count_points_within_circle(x_coords, y_coords)

    def count_points_within_circle(self, x_coords, y_coords):
        number_of_contained_points = 0
        for i in range(len(x_coords)):
            if self.contains(x_coords, y_coords, i):
                number_of_contained_points += 1
        return number_of_contained_points

    def contains(self, x_coords, y_coords, i):
        # check if the point is inside the circle
        delta_x = x_coords[i] - self.center.x
        delta_y = y_coords[i] - self.center.y
        return square(delta_x) + square(delta_y) <= square(self.radius.value)

    def move_to(self, x, y):
        self.center = Point(x, y)

    def resize(self, r):
        self.r = r
        self.radius = Radius(r)

    def format(self):
        return f'circle: {{\n\tcenter: ({self.center.x},{self.center.y}) \n\tradius: {self.radius.value} \n\tcolor: {self.color.get_color_formatted(False)} \n}}'
