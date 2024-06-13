import numpy as np


class LsystemFractal:
    """
    Lsystem implementation of fractals (see compgraph Lab3)

    Now there is no Animation and only radians
    """

    def __init__(self, axiom: str, rules: dict, fi: float, dfi: float, *args):
        """
        Initiates Lsystem fractal with given parameters but before checks if parameters are correct

        # Parameters:
        axiom: string (starting L-axiom)
        rules: dict (rules for how to change each letter (not specific symbol) in iteration)
        max_iterations: int (How many iterations)
        fi: float (starting angular) (now only radians)
        dfi: float (angular velocity) (now only radians)
        """

        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [str, dict, float, float]  # Change if count of arguments changes
        self.check_args(axiom, rules, fi, dfi)

        self.axiom = axiom
        self.rules = rules
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

    def generate_points(self, iteration):
        """
        Generates specified iteration of Lsystem fractal

        # Returns:
        (N+1 shape, N+1 shape) arrays of x and y coordinates
        """
        result = self.axiom
        for iteration in range(iteration):
            new_axiom = ''
            for word_place in range(len(result)):
                if result[word_place] in self.rules.keys():
                    new_axiom += self.rules[self.axiom[word_place]]
                else:
                    new_axiom += result[word_place]
            result = new_axiom

        N = len(result)
        L = 2
        x = np.zeros(N+1)
        y = np.zeros(N+1)
        for i in range(N):
            x[i+1] = x[i]
            y[i+1] = y[i]
            if result[i] == 'F':
                x[i+1] += L*np.cos(self.fi)
                y[i+1] += L*np.sin(self.fi)
            elif result[i] == '+':
                self.fi += self.dfi
            elif result[i] == '-':
                self.fi -= self.dfi
        return x, y
