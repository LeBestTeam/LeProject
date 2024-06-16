import numpy as np
import matplotlib.pyplot as plt

class CardioidCurve:
    """
    Generate points for a Cardioid curve
    """
    def __init__(self, a: float):
        """
        Initialize the Cardioid curve with the given parameter, but before checks if parameters are correct

        # Parameters:
        a: float - the coefficient defining the size of the cardioid
        """
        self.check_args(a)
        self.a = a

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        expected_types = [float]
        if len(args) != 1:
            raise ValueError(f"Expected 1 argument, but got {len(args)}")
        if not isinstance(args[0], expected_types[0]):
            raise ValueError(f"Expected {expected_types[0]} but got {type(args[0])} for argument {args[0]}")

    def generate_points(self):
        """
        Generate the points of the Cardioid curve.

        # Returns:
        A tuple of numpy arrays (x, y) representing the coordinates of the curve.
        """
        t = np.linspace(0, 2 * np.pi, 1000)
        x = self.a * (1 - np.cos(t)) * np.cos(t)
        y = self.a * (1 - np.cos(t)) * np.sin(t)
        return x, y

if __name__ == "__main__":
    cardioid = CardioidCurve(1.0)
    x, y = cardioid.generate_points()
    plt.plot(x, y)
    plt.show()