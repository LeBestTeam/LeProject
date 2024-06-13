import numpy as np


class MandelbrotSet:
    """
    Builds Mandelbrot set fractal
    """

    def __init__(self, threshold: float, width: int, height: int):
        """
        Initializes Mandelbrot set fractal with given parameters

        Parameters:
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.check_args(threshold, width, height)

        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self,*args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        if len(args) != 4:
            raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5") 

        expected_types = [float, int, int]
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self, iterations):
        """
        Generates points for Mandelbrot set fractal.

        Returns:
        numpy array with shape (width, height) containing the number of iterations for each point.
        """
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        Z = np.zeros(C.shape, dtype=complex)
        result = np.zeros(Z.shape, dtype=int)

        for _ in range(self.iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = Z[mask] ** 2 + C[mask]
            result += mask

        return result
