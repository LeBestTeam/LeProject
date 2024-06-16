import numpy as np
import matplotlib.pyplot as plt

class MorphingFractal:
    """
    Generate points for complex fractals
    """

    def __init__(self, fractal_type: str, parameter: complex or int, max_iterations: int = None, threshold: float = 2.0, width: int = 1000, height: int = 1000):
        """
        Initialize the fractal with the given parameters,  but before checks if parameters are correct

        # Parameters:
        fractal_type: str - the type of fractal ('Julia', 'Mandelbrot', 'Multibrot', 'BurningShip', 'Tricorn').
        parameter: complex or int - the parameter for the fractal (complex for Julia, int for Multibrot exponent).
        max_iterations: int - the maximum number of iterations.
        threshold: float - the threshold for fractal calculation.
        width: int - the width of the generated fractal image.
        height: int - the height of the generated fractal image.
        """
        self.check_args(fractal_type, parameter, max_iterations, threshold, width, height)
        self.fractal_type = fractal_type
        self.c = parameter if fractal_type in ["Julia", "SinJulia","HyperbolicTangent"] else None
        self.exponent = parameter if fractal_type == "Multibrot" else 2
        self.max_iterations = max_iterations if fractal_type in ["Julia", "Multibrot", "SinJulia", "HyperbolicTangent"] else parameter
        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """

        fractal_type, parameter, max_iterations, threshold, width, height = args

        valid_fractal_types = ["Julia", "Mandelbrot", "Multibrot", "BurningShip", "Tricorn", "SinJulia", "HyperbolicTangent"]
        if fractal_type not in valid_fractal_types:
            raise ValueError(f"Invalid fractal type '{fractal_type}'. Valid types are: {valid_fractal_types}")
        if not isinstance(fractal_type, str):
            raise TypeError("fractal_type must be a string")

        if not isinstance(parameter, (complex, int)):
            raise TypeError("parameter must be a complex number or an integer")

        if max_iterations is not None and not isinstance(max_iterations, int):
            raise TypeError("max_iterations must be an integer or None")

        if not isinstance(threshold, float):
            raise TypeError("threshold must be a float")

        if not isinstance(width, int) or width <= 0:
            raise ValueError(f"width must be a positive integer")
        
        if not isinstance(height, int) or height <= 0:
            raise ValueError(f"height must be a positive integer")
        
    def generate_points(self):
        """
        Generate the points of the fractal

        # Returns:
        A numpy array representing the iterations for each point in the fractal
        """
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        if self.fractal_type in ["Julia", "SinJulia", "HyperbolicTangent"]:
            Z = C
            c = self.c
        else:
            Z = np.zeros(C.shape, dtype=complex)
            c = C

        result = np.zeros(Z.shape, dtype=int)
        mask = np.ones(Z.shape, dtype=bool)

        for _ in range(self.max_iterations):
            if self.fractal_type == "Julia":
                Z[mask] = Z[mask] ** 2 + c
            elif self.fractal_type == "Mandelbrot":
                Z[mask] = Z[mask] ** 2 + C[mask]
            elif self.fractal_type == "Multibrot":
                Z[mask] = Z[mask] ** self.exponent + C[mask]
            elif self.fractal_type == "BurningShip":
                Z[mask] = (np.abs(Z[mask].real) + 1j * np.abs(Z[mask].imag)) ** 2 + C[mask]
            elif self.fractal_type == "Tricorn":
                Z[mask] = np.conj(Z[mask] ** 2) + C[mask]
            elif self.fractal_type == "SinJulia":
                Z[mask] = np.sin(Z[mask] ** 2) + c
            elif self.fractal_type == "HyperbolicTangent":
                Z[mask] = np.tanh(Z[mask] ** 2) + c
                
            mask = np.abs(Z) < self.threshold
            result[mask] += 1

        return result

if __name__ == "__main__":
    fractal = MorphingFractal("Julia", complex(-0.4, 0.6), 100, 2.0, 1000, 1000)
    #fractal = MorphingFractal("Multibrot", 5, 100, 2.0, 1000, 1000)
    #fractal = MorphingFractal("SinJulia", complex(-0.4, 0.6), 100, 2.0, 1000, 1000)
    #fractal = MorphingFractal("HyperbolicTangent", complex(0.1, 0.1), 100, 2.0, 1000, 1000)
    iterations = fractal.generate_points()
    plt.imshow(iterations, cmap='inferno', extent=(-2, 2, -2, 2))
    plt.show()