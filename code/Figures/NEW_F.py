import numpy as np

class BurningShipFractal:
    def __init__(self, max_iterations: int, threshold: float, width: int, height: int):
        """
        Initializes Burning Ship fractal with given parameters.
        
        Parameters:
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def generate_points(self):
        """
        Generates points for Burning Ship fractal.
        
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
        iterations = np.zeros(Z.shape, dtype=int)

        for i in range(self.max_iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = (np.abs(Z[mask].real) + 1j * np.abs(Z[mask].imag)) ** 2 + C[mask]
            iterations += mask

        return iterations
    
class MultibrotFractal:
    def __init__(self, exponent: int, max_iterations: int, threshold: float, width: int, height: int):
        self.exponent = exponent
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def generate_points(self):
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        Z = np.zeros(C.shape, dtype=complex)
        iterations = np.zeros(Z.shape, dtype=int)

        for i in range(self.max_iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = Z[mask] ** self.exponent + C[mask]
            iterations += mask

        return iterations
    
class TricornFractal:
    def __init__(self, max_iterations: int, threshold: float, width: int, height: int):
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def generate_points(self):
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        Z = np.zeros(C.shape, dtype=complex)
        iterations = np.zeros(Z.shape, dtype=int)

        for i in range(self.max_iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = np.conj(Z[mask] ** 2) + C[mask]
            iterations += mask

        return iterations