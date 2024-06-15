import numpy as np


class DefaultPolynomialFunction:
    def __init__(self, start: float, stop: float, polynom: list, step: float, *args):
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [float, float, list, float]  # Change if count of arguments changes
        self.check_args(start, stop, polynom, step)

        self.start = start
        self.stop = stop
        self.polynom = polynom
        self.step = step

    def check_args(self, *args):
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(
                    f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")

    def generate_points(self, iteration):
        x = np.array(range(self.start, self.stop + self.step, self.step))
        y = np.zeros(len(range(self.start, self.stop + self.step, self.step)))
        for i in range(len(self.polynom)):
            y += (x ** i) * self.polynom[i]
        return x, y
