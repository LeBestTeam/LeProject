import numpy as np
import matplotlib.pyplot as plt


class AffineFractal:
    """
    Build fractals using affine transformation (see compgraph Lab4)
    """
    def __init__(self, list_of_lists_of_parameter: list, skip_first_n_points: int=10**2, standart_type:bool =True, *args):
        """
        Initiates affine fractal with given parameters but before checks if parameters are correct

        # Parameters:
        list_of_lists_of_parameter: list (list with lists in it (For a,b,c,d,e,f and, if needed, p))
        skip_first_n_points: int (skip first n points of the output)
        standart_type: bool (if true -- Decart, if false -- Polar coordinates)
        """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [list, int, bool]
        self.check_args(list_of_lists_of_parameter, skip_first_n_points, standart_type)

        self.skip_first_n_points = skip_first_n_points
        self.standart_type = standart_type
        if self.standart_type:
            if len(list_of_lists_of_parameter) == 7:
                self.a, self.b, self.c, self.d, self.e, self.f, self.p = list_of_lists_of_parameter
            else:
                self.a, self.b, self.c, self.d, self.e, self.f = list_of_lists_of_parameter
                self.p = [1/len(self.a)] * len(self.a)
        else:
            if len(list_of_lists_of_parameter) == 7:
                self.r, self.s, self.t, self.fi, self.e, self.f, self.p = list_of_lists_of_parameter
            else:
                self.r, self.s, self.t, self.fi, self.e, self.f = list_of_lists_of_parameter
                self.p = [1/self.r.__len__()] * len(self.r)

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
        """
        result = np.array(
            [[0.0, 0.0]]*iteration
        )
        size_of_variation = len(self.p)
        if self.standart_type:
            for i in range(iteration-1): # how to handle 'iteration = 0'? It should return starting configuration
                variant = np.random.choice(size_of_variation, 1, p=self.p)
                variant = variant[0]
                xk = self.a[variant]*result[i, 0] + self.b[variant]*result[i, 1] + self.e[variant]
                yk = self.c[variant]*result[i, 0] + self.d[variant]*result[i, 1] + self.f[variant]
                result[i+1] = [xk, yk]
                # i += 1
        else:
            for i in range(iteration-1):
                variant = np.random.choice(size_of_variation, 1, p=self.p)
                variant = variant[0]
                xk = self.r[variant]*np.cos(self.t[variant])*result[i, 0] - self.s[variant]*np.sin(self.fi[variant])*result[i, 1] + self.e[variant]
                yk = self.r[variant]*np.sin(self.t[variant])*result[i, 0] + self.s[variant]*np.cos(self.fi[variant])*result[i, 1] + self.f[variant]
                result[i+1] = [xk, yk]
                # i += 1

        return result[self.skip_first_n_points:, 0], result[self.skip_first_n_points:, 1]


if __name__ == "__main__":
    x, y = AffineFractal([
        [1.0, -0.1],
        [0.2, -1.0],
        [-0.3, 0.4],
        [0.7, 0.2],
        [0.5, -0.4],
        [-0.2, 0.5]
    ]).generate_points(4*10**4)

    plt.plot(x, y, marker='o', linestyle='', markersize=0.6)
    plt.show()
