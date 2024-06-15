import numpy as np
import matplotlib.pyplot as plt

class MorphingFractal:
    def __init__(self, fractal_type: str, parameter: complex or int, max_iterations: int = None, threshold: float = 2.0, width: int = 1000, height: int = 1000):
        self.fractal_type = fractal_type
        self.c = parameter if fractal_type == "Julia" else None
        self.exponent = parameter if fractal_type == "Multibrot" else 2
        self.max_iterations = max_iterations if fractal_type in ["Julia",  "Multibrot"] else (parameter if fractal_type == "Mandelbrot" or "BurningShip" or "Tricorn" else max_iterations)
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

        if self.fractal_type == "Julia":
            Z = C
            c = self.c
        else:
            Z = np.zeros(C.shape, dtype=complex)
            c = C

        iterations = np.zeros(Z.shape, dtype=int)

        for i in range(self.max_iterations):
            if self.fractal_type == "Julia":
                mask = np.abs(Z) < self.threshold
                Z[mask] = Z[mask] ** 2 + c
            elif self.fractal_type == "Mandelbrot":
                mask = np.abs(Z) < self.threshold
                Z[mask] = Z[mask] ** 2 + C[mask]
            elif self.fractal_type == "Multibrot":
                mask = np.abs(Z) < self.threshold
                Z[mask] = Z[mask] ** self.exponent + C[mask]
            elif self.fractal_type == "BurningShip":
                mask = np.abs(Z) < self.threshold
                Z[mask] = (np.abs(Z[mask].real) + 1j * np.abs(Z[mask].imag)) ** 2 + C[mask]
            elif self.fractal_type == "Tricorn":
                mask = np.abs(Z) < self.threshold
                Z[mask] = np.conj(Z[mask] ** 2) + C[mask]
            iterations[mask] += 1

        return iterations


