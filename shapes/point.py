import math


def square(value):
    return value ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def format(self):
        return f'({self.x},{self.y})'

    def distance_to(self, point):
        delta_x = point.x - self.x
        delta_y = point.y - self.y
        return math.sqrt(square(delta_x) + square(delta_y))
