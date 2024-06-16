import numpy as np
import matplotlib.pyplot as plt

class LissajousCurve:
    """
    Generate points for a Lissajous curve 
    """
    def __init__(self,  a: float, b: float, delta: float):
        """
        Initialize the Lissajous curve with given parameters, but before checks if parameters are correct

        # Parameters:
        a: float - the coefficient for the x component
        b: float - the coefficient for the y component
        delta: float - the phase shift for the x component
        """  
        self.check_args(a, b, delta)
        self.a = a
        self.b = b
        self.delta = delta

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        a, b, delta = args
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("Arguments a, b, and delta must be numeric")
                
    def generate_points(self):
        """
        Generate the points of the Lissajous curve.

        # Returns:
        A tuple of numpy arrays (x, y) representing the coordinates of the curve
        """
        t = np.linspace(0, 2 * np.pi, 4000)
        x = self.a * np.sin(self.a * t + self.delta)
        y = self.b * np.sin(self.b * t)
        return x, y

if __name__ == "__main__":
    lissajous = LissajousCurve(5, 4, np.pi/2)
    x, y = lissajous.generate_points()
    plt.plot(x, y)
    plt.show()