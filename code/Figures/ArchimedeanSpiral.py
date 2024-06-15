import numpy as np


class ArchimedeanSpiral:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def check_args(self, *args):
        expected_types = [float, float]
        if len(args) != len(expected_types):
            raise ValueError(f"Expected {len(expected_types)} arguments, but got {len(args)}")
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self):
        t = np.linspace(0, 10 * np.pi, 4000)
        r = self.a + self.b * t
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y