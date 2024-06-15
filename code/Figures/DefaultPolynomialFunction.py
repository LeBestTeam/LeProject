import numpy as np
import matplotlib.pyplot as plt


class DefaultPolynomialFunction:
    """
    Creates regular polygon with constant radius and variable number of verticies
    """
    def __init__(self, start: float, stop: float, polynom: list, *args):
        """
       Initiates DefaultPolynomialFunction with range and polynom but before checks if parameters are correct

       # Parameters:
       start: float (Fitst x)
       stop: float (Last x)
       polynom: list ([a, b, c,...] Multipliers for x**i where i is position in list)
       """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [float, float, list]  # Change if count of arguments changes
        self.check_args(start, stop, polynom)

        self.start = start
        self.stop = stop
        self.polynom = polynom

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(
                    f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")

    def generate_points(self, iteration):
        """
        Returns graph with '1/iteration' precision
        """
        x = np.array([x / iteration + self.start for x in range(int((self.stop - self.start) * iteration))])
        y = np.zeros(len(x))
        for i in range(len(self.polynom)):
            y += (x ** i) * self.polynom[i]
        return x, y


if __name__ == '__main__':
    dots = DefaultPolynomialFunction(-10.0, 10.0, [0, 0, 0, 1]).generate_points(100)
    plt.scatter(dots[0], dots[1])
    plt.show()
