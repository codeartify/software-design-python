from shapes.point import Point


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


class Points:
    def __init__(self, points):
        self.points = points

    @staticmethod
    def create_points_from(x_coords, y_coords):
        validate_coordinates(x_coords, y_coords)
        points = Points.__create_points(x_coords, y_coords)
        return points

    @staticmethod
    def __create_points(x_coords, y_coords):
        points = []
        for i in range(len(x_coords)):
            point = Point(x_coords[i], y_coords[i])
            points.append(point)
        return Points(points)
