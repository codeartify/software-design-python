class Radius:
    def __init__(self, value):
        if value <= 0:
            raise ValueError("Radius needs to be larger 0")
        self.value = value

    def format(self):
        return self.value
