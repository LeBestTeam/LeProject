import numpy as np


class AffineFractal:
    """
    Build fractals using affine transformation (see compgraph Lab4)

    Now there is no Animation and no cosinus and sinus
    """
    def __init__(self, list_of_lists_of_parameter: list, skip_first_n_points: int=10**2, *args):
        """
        Initiates affine fractal with given parameters but before checks if parameters are correct

        # Parameters:
        list_of_lists_of_parameter: list with lists in it (For a,b,c,d,e,f and, if needed, p)
        size_of_fractal: int (How many dots in fractal)
        """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [list, int]
        self.check_args(list_of_lists_of_parameter, skip_first_n_points)

        self.skip_first_n_points = skip_first_n_points
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

    def generate_points(self, iteration):
        """
        Generates dot of affine fractal on each iteration

        # Updates:
        self.axiom each iteration
        """
        result = np.array(
            [[0.0, 0.0]]*iteration
        )
        size_of_variation = len(self.p)
        for i in range(iteration-1):
            variant = np.random.choice(size_of_variation, 1, p=self.p)
            variant = variant[0]
            xk = self.a[variant]*result[i, 0] + self.b[variant]*result[i, 1] + self.e[variant]
            yk = self.c[variant]*result[i, 0] + self.d[variant]*result[i, 1] + self.f[variant]
            result[i+1] = [xk, yk]
            i += 1
        return result[self.skip_first_n_points:, 0], result[self.skip_first_n_points:, 1]