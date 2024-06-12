import numpy as np


class Figure:
    def __init__(self, *args):
        pass

    def check_args(self, *args):
        pass

    def generate_points(self):
        pass


class LsystemFractal(Figure):
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


class AffineFractal(Figure):
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

    def generate_points(self):
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
        return self.xy_array[:, 0], self.xy_array[:, 1]

# class JuliaSet(Figure):
#     """
#     Builds Julia set fractal
#     """

#     def __init__(self, c: complex, max_iterations: int, threshold: float, width: int, height: int):
#         """
#         Initializes Julia set fractal with given parameters but before checks if parameters are correct

#         Parameters:
#         c: complex (constant)
#         max_iterations: int (maximum number of iterations)
#         threshold: float (escape radius)
#         width: int (width of the image)
#         height: int (height of the image)
#         """
#         self.check_args(c, max_iterations, threshold, width, height)

#         self.c = c
#         self.max_iterations = max_iterations
#         self.threshold = threshold
#         self.width = width
#         self.height = height

#     def check_args(self, *args):
#         """
#         Checks if parameters are correct

#         if not - raises ValueError with appropriate message
#         """
#         if len(args) != 5:
#             raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5") 

#         if not isinstance(args[0], complex):
#             raise ValueError(f"Invalid type for argument 'c'. Expected 'complex', got '{type(args[0]).__name__}'")
        
#         if not isinstance(args[1], int) or args[1] <= 0:
#             raise ValueError("max_iterations must be a positive integer")

#         if not isinstance(args[2], float):
#             raise ValueError("threshold must be a float")

#         if not isinstance(args[3], int) or args[3] <= 0:
#             raise ValueError("width must be a positive integer")

#         if not isinstance(args[4], int) or args[4] <= 0:
#             raise ValueError("height must be a positive integer")
        
#     def generate_points(self):
#         """
#         Generates points for Julia set fractal

#         Returns:
#         (x_coords, y_coords): Coordinates of points in the Julia set
#         """
#         x_min, x_max = -2, 2
#         y_min, y_max = -2, 2

#         x = np.linspace(x_min, x_max, self.width)
#         y = np.linspace(y_min, y_max, self.height)

#         X, Y = np.meshgrid(x, y)
#         Z = X + 1j * Y

#         x_coords = []
#         y_coords = []

#         for _ in range(self.max_iterations):
#             mask = np.abs(Z) < self.threshold
#             Z[mask] = Z[mask] ** 2 + self.c

#         mask = np.abs(Z) < self.threshold
#         x_coords = X[mask]
#         y_coords = Y[mask]

#         return x_coords, y_coords

class JuliaSet(Figure):
    """
    Builds Julia set fractal
    """

    def __init__(self, c: complex, max_iterations: int, threshold: float, width: int, height: int):
        """
        Initializes Julia set fractal with given parameters but before checks if parameters are correct

        Parameters:
        c: complex (constant)
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.check_args(c, max_iterations, threshold, width, height)

        self.c = c
        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        if len(args) != 5:
            raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5") 

        expected_types = [complex, int, float, int, int]
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")


    def generate_points(self):
        """
        Generates points for Julia set fractal.

        Returns:
        numpy array with shape (width, height) containing the number of iterations for each point.
        """
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y

        iterations = np.zeros(Z.shape, dtype=int)

        for i in range(self.max_iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = Z[mask] ** 2 + self.c
            iterations += mask

        return iterations
    
class MandelbrotSet(Figure):
    """
    Builds Mandelbrot set fractal
    """

    def __init__(self, max_iterations: int, threshold: float, width: int, height: int):
        """
        Initializes Mandelbrot set fractal with given parameters

        Parameters:
        max_iterations: int (maximum number of iterations)
        threshold: float (escape radius)
        width: int (width of the image)
        height: int (height of the image)
        """
        self.check_args(max_iterations, threshold, width, height)

        self.max_iterations = max_iterations
        self.threshold = threshold
        self.width = width
        self.height = height

    def check_args(self,*args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        if len(args) != 4:
            raise ValueError(f"Wrong number of arguments, {len(args)} provided, expected 5") 

        expected_types = [int, float, int, int]
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self):
        """
        Generates points for Mandelbrot set fractal.

        Returns:
        numpy array with shape (width, height) containing the number of iterations for each point.
        """
        x_min, x_max = -2, 2
        y_min, y_max = -2, 2

        x = np.linspace(x_min, x_max, self.width)
        y = np.linspace(y_min, y_max, self.height)

        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        Z = np.zeros(C.shape, dtype=complex)
        iterations = np.zeros(Z.shape, dtype=int)

        for _ in range(self.max_iterations):
            mask = np.abs(Z) < self.threshold
            Z[mask] = Z[mask] ** 2 + C[mask]
            iterations += mask

        return iterations
    
