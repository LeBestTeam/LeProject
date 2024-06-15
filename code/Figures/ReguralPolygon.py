import numpy as np
import matplotlib.pyplot as plt


class RegularPolygon:
    """
    Creates regular polygon with constant radius and variable number of verticies
    """

    def __init__(self, radius: float, fi: float, overdot: bool = True, *args):
        """
        Initiates RegularPolygon with given radius but before checks if parameters are correct

        # Parameters:
        radius: float (Distance from center to verticies)
        fi: float (Aangle offset)
        overdot: bool (Add extra dot at the end same as the first dot )
        """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [float, float, bool]  # Change if count of arguments changes
        self.check_args(radius, fi, overdot)

        self.radius = radius
        self.fi = fi
        self.overdot = overdot

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(
                    f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")
        if args[0] <= 0:
            raise ValueError("Radius must be positive")
        return 1

    def generate_points(self, iteration: int):
        """
        Returns regular polygon with 'iteration' vertices
        """
        if self.overdot:
            x = np.zeros(iteration + 1)
            y = np.zeros(iteration + 1)
        else:
            x = np.zeros(iteration)
            y = np.zeros(iteration)
        angle = self.fi % np.pi
        d_angle = np.pi * 2 / iteration
        for i in range(iteration):
            x[i], y[i] = self.radius * np.cos(angle), self.radius * np.sin(angle)
            angle += d_angle
        if self.overdot:
            x[-1], y[-1] = x[0], y[0]
        return x, y


if __name__ == '__main__':
    dots = RegularPolygon(2.0, 0.1).generate_points(6)
    plt.scatter(dots[0], dots[1])
    plt.show()
