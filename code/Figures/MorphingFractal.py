import numpy as np


class MorphingFractal:
    """
    Builds fractals using morphing techniques
    """

    def __init__(self, initial_function, max_iterations, threshold, width, height):
        """
        Initializes the fractal generator with given parameters.

        Parameters:
        initial_function: callable (the initial function to apply)
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.check_args(initial_function, max_iterations, threshold, width, height)

        self.initial_function = initial_function
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self, *args):
        """
        Checks if parameters are correct

        If not, raises ValueError with an appropriate message
        """
        if len(args) != 5:
            raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5")

        expected_types = [callable, int, float, int, int]
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self):
        """
        Generates points for the fractal.

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

        for i in range(self.max_iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = self.initial_function(Z[mask])
            iterations += mask

        return iterations