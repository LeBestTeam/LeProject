from Figure import *
import warnings
import numpy as np


class LFractalBuilder(FigureBuilder):
    def __init__(self, axiom: str, rules: dict, fi: float, dfi: float, f_step=2, *args):
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

        self.__axiom = axiom
        self.__rules = rules
        self.__fi = fi
        self.__dfi = dfi
        self.__f_step = f_step

        self.__check_succes = None
        self.__check_args()

    def __check_args(self):
        """
        checks arguments after __init__ and in get_figure
        """
        check_success = True

        # check types
        arg_types = [[str], [dict], [float, int], [float, int], [float, int]]
        args = [self.__axiom, self.__rules, self.__fi, self.__dfi, self.__f_step]
        for i in range(len(args)):
            if not args[i] in arg_types[i]:
                check_success = False
                warnings.warn(f"WARNING: wrong type of {args[i]=}. Must be one of these: {arg_types[i]}")

        # check values
        if self.__axiom == "":
            check_success = False
            warnings.warn("WARNING: axiom must not be empty")
        if self.__rules == {}:
            check_success = False
            warnings.warn("WARNING: rules must not be empty")

        if check_success:
            self.__check_succes = True
            return 1
        else:
            raise Exception("EXCEPTION: check failed")

    def get_figure(self):
        """
        default functionality example
        """

        if self.check_succes is None:
            import warnings
            warnings.warn("Check has not been completed yet")
            return 0
        if self.check_succes:
            figure = Figure()
            figure.__axiom = self.__axiom  # add copy.deepcopy?
            figure.__rules = self.__rules
            figure.__fi = self.__fi
            figure.__dfi = self.__dfi
            figure.__f_step = self.__f_step

            def generate_points(self, iteration):
                # init

                final_l_string = []
                for iter in range(iteration):
                    new_axiom = ''
                    for word_place in range(len(self.__axiom)):
                        if self.__axiom[word_place] in self.__rules.keys():
                            new_axiom += self.__rules[self.__axiom[word_place]]
                        else:
                            new_axiom += self.__axiom[word_place]
                    final_l_string = new_axiom

                N = len(final_l_string)
                L = self.__f_step
                fi = self.__fi
                x = np.zeros(N + 1)  # wtf
                y = np.zeros(N + 1)  # should be: np.zeros("Number of F")
                for i in range(N):
                    x[i + 1] = x[i]
                    y[i + 1] = y[i]
                    if final_l_string[i] == 'F':
                        x[i + 1] += L * np.cos(fi)
                        y[i + 1] += L * np.sin(fi)
                    elif final_l_string[i] == '+':
                        fi += self.__dfi
                    elif final_l_string[i] == '-':
                        fi -= self.__dfi
                return x, y

            figure.generate_points = generate_points
            return figure
        else:
            import warnings
            warnings.warn("Chack has failed")
            return 0
