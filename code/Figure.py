import numpy as np


class Figure:
    def __init__(self, *args):
        pass

    def generate_points(self):
        pass


class LsystemFractal(Figure):
    def __init__(self, axiom: str, rules: dict, max_iterations: int, fi: float, dfi: float, *args):
        self.list_to_check = [str, dict, int, float, float]  # Change if count of arguments changes
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
                raise ValueError(f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")

    def generate_points(self):
        """
        Generates more and more of Lsystem fractal on each iteration

        # Updates:
        self.axiom each iteration

        Calculates all coordinates of Lsystem fractal

        # Returns:
        (N+1 shape, N+1 shape) arrays of x and y coordinates
        """
        for iteration in range(self.max_iterations):
            new_axiom = ''
            for word_place in range(len(self.axiom)):
                if self.axiom[word_place] in self.rules.keys():
                    new_axiom += self.rules[self.axiom[word_place]]
                else:
                    new_axiom += self.axiom[word_place]
            self.axiom = new_axiom

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
