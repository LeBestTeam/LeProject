import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class Fractal:  # pragma: no cover
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

    def generate(self):
        pass

    def draw(self):
        pass


class LFractal(Fractal):
    """
    Lsystem implementation of fractals (see compgraph Lab3)

    Now there is no Animation and only radians
    """
    def __init__(self, axiom: str, rules: dict, max_iterations: int, fi: float, dfi: float, *args):
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
        self.list_to_check = [str, dict, int, float, float]  # Change if count of arguments changes
        if type(fi) is int:
            try:
                fi = float(fi)
            except ValueError:
                raise ValueError(f"Wrong fi, which is {type(fi)} type, expected int or float type")
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

    def build(self, **kwargs):
        """
        Builds (generates and draws) Lsystem fractal
        """
        self.generate()
        self.draw(**kwargs)

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

    def draw(self, **kwargs):
        """
        Plots Lsystem fractal
        """
        fig, ax = plt.subplots()
        x, y = self.calculate()
        ax.plot(x, y)

        if "show" not in kwargs:
            plt.show()
        else:
            if kwargs["show"]:
                plt.show()


class AffineFractal(Fractal):
    """
    Build fractals using affine transformation (see compgraph Lab4)

    Now there is no Animation and no cosinus and sinus
    """
    def __init__(self, list_of_lists_of_parameter: list, size_of_fractal: int = 10**4, *args):
        """
        Initiates affine fractal with given parameters but before checks if parameters are correct

        # Parameters:
        list_of_lists_of_parameter: list with lists in it (For a,b,c,d,e,f and, if needed, p)
        size_of_fractal: int (How many dots in fractal)
        """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [list, int]
        self.check_args(list_of_lists_of_parameter, size_of_fractal)
        self.size = size_of_fractal
        self.xy_array = np.array(
            [[0.0, 0.0]]*self.size
        )
        # From here it is uses my representation of affine transformation (a = first list(row), b = second list(row) and others)
        if len(list_of_lists_of_parameter) == 7:
            self.a, self.b, self.c, self.d, self.e, self.f, self.p = list_of_lists_of_parameter
        else:
            self.a, self.b, self.c, self.d, self.e, self.f = list_of_lists_of_parameter
            self.p = [1/len(self.a)] * len(self.a)

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")

        previous_parameter = None
        for parameter in args[0]:
            if type(parameter) is not list:  # checks if what it received is list
                raise ValueError(f"Wrong parameter {parameter}, which is {type(parameter)} type, expected list type")

            for parameter_index in range(len(parameter)):  # checks if what it received is list where each element is int or float
                if type(parameter[parameter_index]) is not int and type(parameter[parameter_index]) is not float:
                    raise ValueError(f"Wrong parameter {parameter[parameter_index]}, which is {type(parameter[parameter_index])} type, expected int or float type")

            if previous_parameter is not None: # checks len of each parameter
                if len(previous_parameter) != len(parameter):
                    raise ValueError(f"Wrong length of parameter {parameter} in row {args[0].index(parameter)}, expected {len(previous_parameter)}")
            if len(args[0]) != 6 and len(args[0]) != 7:
                raise ValueError(f"Wrong size of list {args[0]} whose len is: {len(args[0])}, expected 6 or 7")
            previous_parameter = parameter

    def build(self, **kwargs):
        """
        Builds (generates and draws) affine fractal
        """
        self.generate()
        self.draw(**kwargs)

    def generate(self):
        """
        Generates dot of affine fractal on each iteration

        # Updates:
        self.axiom each iteration
        """
        size_of_variation = len(self.p)
        for i in range(self.size-1):
            variant = np.random.choice(size_of_variation, 1, p=self.p)
            variant = variant[0]
            xk = self.a[variant]*self.xy_array[i, 0] + self.b[variant]*self.xy_array[i, 1] + self.e[variant]
            yk = self.c[variant]*self.xy_array[i, 0] + self.d[variant]*self.xy_array[i, 1] + self.f[variant]
            self.xy_array[i+1] = [xk, yk]
            i += 1


    def draw(self, **kwargs):
        """
        Plots affine fractal
        """
        plt.scatter(self.xy_array[:, 0], self.xy_array[:, 1], s=1)
        if "show" not in kwargs:
            plt.show()
        else:
            if kwargs["show"]:
                plt.show()


class MatrixFractal(Fractal):
    """
    Build fractals using matrix (see compgraph 2024-02-27)
    """
    def __init__(self, patern: list, max_iterations: int, *args):
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.patern = np.matrix(patern)
        self.max_iterations = max_iterations

    def check_args(self):
        raise NotImplementedError()

    def build(self, **kwargs):
        self.generate()
        self.draw(**kwargs)

    def calculate(self):
        raise NotImplementedError()

    def generate(self):
        self.matrix_fractal = 1
        for iteration in range(self.max_iterations):
            pass  # do somethings

    def draw(self, **kwargs):
        pass  # do somethings
        # Image.fromarray(self.S).show()


if __name__ == '__main__':
    axiom = "F+F+X+F"
    rules = {"F": "FF+X++F+F", "X": "F-X++F-F"}
    max_iter = 3
    fi = 0
    dfi = np.pi/2

    L = LFractal(axiom, rules, max_iter, fi, dfi).build()

    #     af = AffineFractal([
    #         [1.0, -0.1],
    #         [0.2, -1.0],
    #         [-0.3, 0.4],
    #         [0.7, 0.2],
    #         [0.5, -0.4],
    #         [-0.2, 0.5]
    # ]).build()
    # mf = MatrixFractal([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1).build()
