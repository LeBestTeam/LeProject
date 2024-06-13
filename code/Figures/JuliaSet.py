import numpy as np


class JuliaSet:
    """
    Builds Julia set fractal
    """

    def __init__(self, c: complex, threshold: float, width: int, height: int):
        """
        Initializes Julia set fractal with given parameters but before checks if parameters are correct

        Parameters:
        c: complex (constant)
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.check_args(c, threshold, width, height)

        self.c = c
        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        expected_types = [complex, float, int, int]

        if len(args) != len(expected_types):
            raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected {len(expected_types)}")

        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self, iteration):
        """
        Generates points for Julia set fractal.

        Returns:
        numpy array with shape (width, height) containing the number of iterations for each point.
        """
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y

        result = np.zeros(Z.shape, dtype=int)

        for i in range(iteration):
            mask = np.abs(Z) < self.threshold
            Z[mask] = Z[mask] ** 2 + self.c
            result += mask

        return result

# class JuliaSet(Figure):
#     """
#     Builds Julia set fractal
#     """

#     def __init__(self, c: complex, max_iterations: int, threshold: float, width: int, height: int):
#         """
#         Initializes Julia set fractal with given parameters but before checks if parameters are correct

#         Parameters:
#         c: complex (constant)
#         max_iterations: int (maximum number of iterations)
#         threshold: float (escape radius)
#         width: int (width of the image)
#         height: int (height of the image)
#         """
#         self.check_args(c, max_iterations, threshold, width, height)

#         self.c = c
#         self.max_iterations = max_iterations
#         self.threshold = threshold
#         self.width = width
#         self.height = height

#     def check_args(self, *args):
#         """
#         Checks if parameters are correct

#         if not - raises ValueError with appropriate message
#         """
#         if len(args) != 5:
#             raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5") 

#         if not isinstance(args[0], complex):
#             raise ValueError(f"Invalid type for argument 'c'. Expected 'complex', got '{type(args[0]).__name__}'")
        
#         if not isinstance(args[1], int) or args[1] <= 0:
#             raise ValueError("max_iterations must be a positive integer")

#         if not isinstance(args[2], float):
#             raise ValueError("threshold must be a float")

#         if not isinstance(args[3], int) or args[3] <= 0:
#             raise ValueError("width must be a positive integer")

#         if not isinstance(args[4], int) or args[4] <= 0:
#             raise ValueError("height must be a positive integer")
        
#     def generate_points(self):
#         """
#         Generates points for Julia set fractal

#         Returns:
#         (x_coords, y_coords): Coordinates of points in the Julia set
#         """
#         x_min, x_max = -2, 2
#         y_min, y_max = -2, 2

#         x = np.linspace(x_min, x_max, self.width)
#         y = np.linspace(y_min, y_max, self.height)

#         X, Y = np.meshgrid(x, y)
#         Z = X + 1j * Y

#         x_coords = []
#         y_coords = []

#         for _ in range(self.max_iterations):
#             mask = np.abs(Z) < self.threshold
#             Z[mask] = Z[mask] ** 2 + self.c

#         mask = np.abs(Z) < self.threshold
#         x_coords = X[mask]
#         y_coords = Y[mask]

#         return x_coords, y_coords
