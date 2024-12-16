import unittest

from shapes.circle import Circle
from shapes.points import Points


class TestCircle(unittest.TestCase):

    def test_should_always_have_a_radius_larger_0(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, 0)
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_should_handle_coordinates_of_unequal_length(self):
        circle = Circle(0, 0, 2)
        x_coordinates = [2, 3, 4, -12, -20]
        y_coordinates = [8, 20, 15, -4]
        with self.assertRaises(ValueError):
            circle.count_contained_points(Points.create_points_from(x_coordinates, y_coordinates))

    def test_should_handle_empty_x_coordinates(self):
        circle = Circle(0, 0, 2)
        y_coordinates = [8, 20, 15, -4]
        with self.assertRaises(ValueError):
            circle.count_contained_points(Points.create_points_from(None, y_coordinates))
        with self.assertRaises(ValueError):
            coords = []
            circle.count_contained_points(Points.create_points_from(coords, y_coordinates))

    def test_should_handle_empty_y_coordinates(self):
        circle = Circle(0, 0, 2)
        x_coordinates = [8, 20, 15, -4]
        with self.assertRaises(ValueError):
            circle.count_contained_points(Points.create_points_from(x_coordinates, None))
        with self.assertRaises(ValueError):
            coords = []
            circle.count_contained_points(Points.create_points_from(x_coordinates, coords))

    def test_should_count_contained_points(self):
        circle = Circle(5, -5, 10)
        x_coordinates = [2, 1, 3, 8, 4, -12, -20, -4]
        y_coordinates = [8, 1, 20, -4, 15, -4, -20, -4]
        self.assertEqual(3, circle.count_contained_points(Points.create_points_from(x_coordinates, y_coordinates)))

    def test_should_count_contained_points_when_moved_to_new_location(self):
        circle = Circle(0, 0, 20)
        x_coordinates = [2, 3, 4, -12, -20]
        y_coordinates = [8, 20, 15, -4, -20]
        self.assertEqual(3, circle.count_contained_points(Points.create_points_from(x_coordinates, y_coordinates)))
        circle.move_to(-30, -30)
        self.assertEqual(1, circle.count_contained_points(Points.create_points_from(x_coordinates, y_coordinates)))

    def test_should_count_contained_points_when_resized_for_new_area(self):
        circle = Circle(0, 0, 20)
        x_coordinates = [2, 3, 4, -12, -20]
        y_coordinates = [8, 20, 15, -4, -20]
        self.assertEqual(3, circle.count_contained_points(Points.create_points_from(x_coordinates, y_coordinates)))
        circle.resize(40)
        self.assertEqual(5, circle.count_contained_points(Points.create_points_from(x_coordinates, y_coordinates)))
        circle.resize(1)
        self.assertEqual(0, circle.count_contained_points(Points.create_points_from(x_coordinates, y_coordinates)))

    def test_should_format_location_and_radius_as_string(self):
        circle = Circle(1, 4, 7)
        expected_format = (
            "circle: {\n"
            "\tcenter: (1,4) \n"
            "\tradius: 7 \n"
            "\tcolor: Green \n"
            "}"
        )
        self.assertEqual(expected_format, circle.format())
