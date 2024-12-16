from shapes.color import Color
from shapes.shape import Shape


class Circle(Shape):
    def __init__(self, x, y, r):
        if r <= 0:
            raise ValueError("Radius needs to be larger 0")
        self.x = x
        self.y = y
        self.r = r
        self.color = Color("Green")
        self.number_of_contained_points = 0

    def count_contained_points(self, x_coords, y_coords):
        self.number_of_contained_points = 0
        if x_coords is not None:
            if len(x_coords) > 0:
                if y_coords is not None:
                    if len(y_coords) > 0:
                        if len(x_coords) == len(y_coords):
                            for i in range(len(x_coords)):
                                self.contains(x_coords, y_coords, i)
                        else:
                            raise ValueError("Not every provided x coordinate has a matching y coordinate")
                    else:
                        raise ValueError("y coordinates are empty")
                else:
                    raise ValueError("y coordinates are empty")
            else:
                raise ValueError("x coordinates are empty")
        else:
            raise ValueError("x coordinates are empty")
        return self.number_of_contained_points

    def contains(self, x_coords, y_coords, i):
        result = (x_coords[i] - self.x) * (x_coords[i] - self.x) + (y_coords[i] - self.y) * (y_coords[i] - self.y) <= self.r * self.r
        if result:
            self.number_of_contained_points += 1
        return result

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def resize(self, r):
        self.r = r

    def format(self):
        return f'circle: {{\n\tcenter: ({self.x},{self.y}) \n\tradius: {self.r} \n\tcolor: {self.color.get_color_formatted(False)} \n}}'
