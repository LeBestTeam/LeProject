import matplotlib.pyplot as plt
import numpy as np


class Fractal:
    """
    Interface to use all fractals in app using same function

    Seems to be not used in app `but can be a good template`
    """
    def __init__(self):
        pass

    def check_args(self):
        pass

    def build(self):
        pass

    def calculate(self):
        pass

    def generate(self):
        pass

    def draw(self):
        pass


class LFractal(Fractal):
    """Lsystem implementation of fractals"""
    def __init__(self, axiom: str, rules: dict, max_iterations: int, fi: float, dfi: float, *args):
        """
        Initiates Lsystem fractal with given parameters but before checks if parameters are correct

        # Parameters:
        axiom: string (starting L-axiom)
        rules: dict (rules for how to change each letter (not specific symbol) in iteration)
        max_iterations: int (How many iterations)
        fi: float (starting angular)
        dfi: float (angular velocity)
        """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [str, dict, int, float, float]  # Change if count of arguments changes
        if type(fi) is int:
            try:
                fi = float(fi)
            except ValueError:
                raise ValueError(f"Wrong fi, which is {type(fi)} type, excepted int or float type")
        self.check_args(axiom, rules, max_iterations, fi, dfi)
        self.axiom = axiom
        self.rules = rules
        self.max_iterations = max_iterations
        self.fi = fi
        self.dfi = dfi

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, excepted {self.list_to_check[argument_index]} type")

    def build(self):
        """
        Builds (generates and draws) Lsystem fractal
        """
        self.generate()
        self.draw()

    def calculate(self):
        """
        Calculates all coordinates of Lsystem fractal

        # Returns:
        (N+1 shape, N+1 shape) arrays of x and y coordinates
        """
        N = len(self.axiom)
        L = 2
        x = np.zeros(N+1)
        y = np.zeros(N+1)
        for i in range(N):
            x[i+1] = x[i]
            y[i+1] = y[i]
            if self.axiom[i] == 'F':
                x[i+1] += L*np.cos(self.fi)
                y[i+1] += L*np.sin(self.fi)
            elif self.axiom[i] == '+':
                self.fi += self.dfi
            elif self.axiom[i] == '-':
                self.fi -= self.dfi
        return x, y

    def generate(self):
        """
        Generates more and more of Lsystem fractal on each iteration

        # Updates:
        self.axiom each iteration
        """
        for iteration in range(self.max_iterations):
            new_axiom = ''
            for word_place in range(len(self.axiom)):
                if self.axiom[word_place] in self.rules.keys():
                    new_axiom += self.rules[self.axiom[word_place]]
                else:
                    new_axiom += self.axiom[word_place]
            self.axiom = new_axiom

    def draw(self):
        fig, ax = plt.subplots()
        x, y = self.calculate()
        ax.plot(x, y)

        plt.show()


class AffineFractal(Fractal):
    """
    Build fractals using affine transformation (see compgraph Lab4)
    """
    def __init__(self):
        raise NotImplementedError()

    def check_args(self):
        raise NotImplementedError()

    def build(self):
        raise NotImplementedError()

    def calculate(self):
        raise NotImplementedError()

    def generate(self):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()


class MatrixFractal(Fractal):
    """
    Build fractals using matrix (see compgraph 2024-02-27)
    """
    def __init__(self):
        raise NotImplementedError()

    def check_args(self):
        raise NotImplementedError()

    def build(self):
        raise NotImplementedError()

    def calculate(self):
        raise NotImplementedError()

    def generate(self):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()


if __name__ == '__main__':
    axiom = "F+F+X+F"
    rules = {"F": "FF+X++F+F", "X": "F-X++F-F"}
    max_iter = 3
    fi = 0
    dfi = np.pi/2

    L = LFractal(axiom, rules, max_iter, fi, dfi).build()
