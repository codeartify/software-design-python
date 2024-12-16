class Color:
    GREEN = "2"

    def get_color_formatted(self):
        return f"{self.color_as_text} {self.color_as_hex} {self.color_as_rgb_red}:{self.color_as_rgb_green}:{self.color_as_rgb_blue}"

    def __init__(self, color_code):
        self.color_as_text = None
        self.color_as_hex = None
        self.color_as_rgb_red = None
        self.color_as_rgb_green = None
        self.color_as_rgb_blue = None
        self.error_message = ""
        self.convert_text_value_to_rgb_and_hex(color_code)

    def convert_text_value_to_rgb_and_hex(self, color_code):
        self.error_message = ""
        # set to Red
        if color_code == "0":
            self.color_as_text = "Red"
            self.color_as_rgb_red = "255"
            self.color_as_rgb_blue = "0"
            self.color_as_rgb_green = "0"
            self.color_as_hex = "#FF0000"
        elif color_code == "1":
            # set to Blue
            self.color_as_text = "Blue"
            self.color_as_rgb_red = "0"
            self.color_as_rgb_blue = "255"
            self.color_as_rgb_green = "0"
            self.color_as_hex = "#00FF00"
        elif color_code == "2":
            # set to Green
            self.color_as_text = "Green"
            self.color_as_rgb_red = "0"
            self.color_as_rgb_blue = "0"
            self.color_as_rgb_green = "255"
            self.color_as_hex = "#0000FF"
        else:
            self.error_message = "Color not recognized"

    def get_blue(self):
        return self.color_as_rgb_blue

    def get_green(self):
        return self.color_as_rgb_green

    def get_red(self):
        return self.color_as_rgb_red

    def get_error_message(self):
        return self.error_message
