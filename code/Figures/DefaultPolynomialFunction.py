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
        pass

    def generate_points(self, iteration):
        pass