import numpy as np


class CardioidCurve:
    def __init__(self, a: float):
        self.a = a

    def check_args(self, *args):
        expected_types = [float]
        if len(args) != 1:
            raise ValueError(f"Expected 1 argument, but got {len(args)}")
        if not isinstance(args[0], expected_types[0]):
            raise ValueError(f"Expected {expected_types[0]} but got {type(args[0])} for argument {args[0]}")

    def generate_points(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = self.a * (1 - np.cos(t)) * np.cos(t)
        y = self.a * (1 - np.cos(t)) * np.sin(t)
        return x, y