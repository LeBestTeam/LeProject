import numpy as np

class RecurrenceFractal:
    """
    Generates fractals using recurrence relations.
    """

    def __init__(self, a: float, b: float, max_iterations: int, threshold: float, width: int, height: int):
        """
        Initializes the fractal with given parameters.

        Parameters:
        a: float (parameter for recurrence relation)
        b: float (parameter for recurrence relation)
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.a = a
        self.b = b
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

        self.check_args(a, b, max_iterations, threshold, width, height)

    def check_args(self, *args):
        """
        Checks if parameters are correct.

        Raises:
        ValueError: if any parameter is incorrect.
        """
        expected_types = [float, float, int, float, int, int]
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self):
        """
        Generates points for the fractal using recurrence relations.

        Returns:
        numpy array with shape (width, height) containing the number of iterations for each point.
        """
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y

        iterations = np.zeros(Z.shape, dtype=int)
        mask = np.abs(Z) < self.threshold

        for _ in range(self.max_iterations):
            Z[mask] = Z[mask] ** 2 + self.a * Z[mask] + self.b
            mask = np.abs(Z) < self.threshold
            iterations += mask

        return iterations

def sierpinski_function(point, coefficients):
    x, y = point
    a, b, c, d = coefficients
    # Perform the recurrence relation calculations
    if x > y:
        x_new = x + a * y
        y_new = b * x + c * y + d
    else:
        x_new = b * x + c * y + d
        y_new = x + a * y
    return x_new, y_new

def julia_function(point, coefficients):
    x, y = point
    a, b, c, d = coefficients
    return (a * x**2 - b * y**2 + c, 2 * a * b * x * y + d)

def mandelbrot_function(point, coefficients):
    x, y = point
    a, b, c, d = coefficients
    return (a * x**2 - b * y**2 + c, 2 * a * b * x * y + d)