import numpy as np
import matplotlib.pyplot as plt


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

    def generate_points(self, iteration):
        t = np.linspace(0, 10 * np.pi, iteration)
        r = self.a + self.b * t
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y


if __name__ == "__main__":
    archimedean = ArchimedeanSpiral(1, 2)
    x, y = archimedean.generate_points(4000)
    plt.plot(x, y)
    plt.show()
