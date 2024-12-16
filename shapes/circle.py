from shapes.color import Color
from shapes.shape import Shape


def square(value):
    return value * value


class Circle(Shape):
    def __init__(self, x, y, r):
        if r <= 0:
            raise ValueError("Radius needs to be larger 0")
        self.x = x
        self.y = y
        self.r = r
        self.color = Color(Color.GREEN)

    def count_contained_points(self, x_coords, y_coords):
        if x_coords is None or len(x_coords) <= 0:
            raise ValueError("x coordinates are empty")
        if y_coords is None or len(y_coords) <= 0:
            raise ValueError("y coordinates are empty")
        if len(x_coords) != len(y_coords):
            raise ValueError("Not every provided x coordinate has a matching y coordinate")
        number_of_contained_points = 0
        for i in range(len(x_coords)):
            if self.contains(x_coords, y_coords, i):
                number_of_contained_points += 1
        return number_of_contained_points

    def contains(self, x_coords, y_coords, i):
        # check if the point is inside the circle
        delta_x = x_coords[i] - self.x
        delta_y = y_coords[i] - self.y
        return square(delta_x) + square(delta_y) <= square(self.r)

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def resize(self, r):
        self.r = r

    def format(self):
        return f'circle: {{\n\tcenter: ({self.x},{self.y}) \n\tradius: {self.r} \n\tcolor: {self.color.get_color_formatted(False)} \n}}'
