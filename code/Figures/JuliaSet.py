import numpy as np


class JuliaSet:
    """
    Builds Julia set fractal
    """

    def __init__(self, c: complex, max_iterations: int, threshold: float, width: int, height: int):
        """
        Initializes Julia set fractal with given parameters but before checks if parameters are correct

        Parameters:
        c: complex (constant)
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.check_args(c, max_iterations, threshold, width, height)

        self.c = c
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        if len(args) != 5:
            raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5") 

        expected_types = [complex, int, float, int, int]
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self):
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

        iterations = np.zeros(Z.shape, dtype=int)

        for i in range(self.max_iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = Z[mask] ** 2 + self.c
            iterations += mask

        return iterations

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

import numpy as np

class LyapunovFractal:
    """
    Builds Lyapunov fractal.
    """

    def __init__(self, sequence: str, max_iterations: int, threshold: float, width: int, height: int):
        """
        Initializes Lyapunov fractal with given parameters but before checks if parameters are correct

        Parameters:
        sequence: str (sequence of A's and B's)
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.check_args(sequence, max_iterations, threshold, width, height)

        self.sequence = sequence
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        if len(args) != 5:
            raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5") 

        if not isinstance(args[0], str) or not all(c in "AB" for c in args[0]):
            raise ValueError(f"Expected a string of A's and B's but got {args[0]}")
        if not isinstance(args[1], int):
            raise ValueError(f"Expected {int} but got {type(args[1])} for argument {args[1]}")
        if not isinstance(args[2], float):
            raise ValueError(f"Expected {float} but got {type(args[2])} for argument {args[2]}")
        if not isinstance(args[3], int):
            raise ValueError(f"Expected {int} but got {type(args[3])} for argument {args[3]}")
        if not isinstance(args[4], int):
            raise ValueError(f"Expected {int} but got {type(args[4])} for argument {args[4]}")

    def generate_points(self):
        """
        Generates points for Lyapunov fractal.

        Returns:
        numpy array with shape (width, height) containing the number of iterations for each point.
        """
        x_min, x_max = 2.5, 4.0
        y_min, y_max = 2.5, 4.0

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        iterations = np.zeros(X.shape, dtype=int)
        
        for i in range(self.width):
            for j in range(self.height):
                r1, r2 = X[i, j], Y[i, j]
                zn = 0.5
                stable = True
                for k in range(self.max_iterations):
                    if self.sequence[k % len(self.sequence)] == 'A':
                        zn = r1 * zn * (1 - zn)
                    else:
                        zn = r2 * zn * (1 - zn)
                    
                    if zn <= 0 or zn >= 1:
                        stable = False
                        break

                iterations[i, j] = k if stable else self.max_iterations

        return iterations


