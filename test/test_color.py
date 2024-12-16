import unittest

from shapes.color import Color


class TestColor(unittest.TestCase):

    def test_should_format_color_as_text(self):
        red = Color("Red")

        color_formatted = red.get_color_formatted(False)

        self.assertEqual("Red", color_formatted)

    def test_should_format_color_as_text_and_hex_and_rgb(self):
        red = Color("Red")

        color_formatted = red.get_color_formatted(True)

        self.assertEqual("Red #FF0000 255:0:0", color_formatted)

    def test_should_format_green_as_hex_and_rgb(self):
        green = Color("Green")

        color_formatted = green.get_color_formatted(True)

        self.assertEqual("Green #0000FF 0:255:0", color_formatted)

    def test_should_format_blue_as_hex_and_rgb(self):
        blue = Color("Blue")

        color_formatted = blue.get_color_formatted(True)

        self.assertEqual("Blue #00FF00 0:0:255", color_formatted)
