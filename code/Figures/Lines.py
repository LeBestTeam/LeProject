import numpy as np


# class EpicycloidCurve:
#     """
#     Generates points for an epicycloid curve.
#     """

#     def __init__(self, R: float, r: float, d: float):
#         """
#         Initializes the epicycloid curve with given parameters.

#         Parameters:
#         R: float (radius of the fixed circle)
#         r: float (radius of the rolling circle)
#         d: float (distance from the center of the rolling circle to the tracing point)
#         """
#         self.R = R
#         self.r = r
#         self.d = d

#     def check_args(self, *args):
#         """
#         Checks if parameters are correct.
#         """
#         expected_types = [float, float, float]
#         if len(args) != len(expected_types):
#             raise ValueError(f"Expected {len(expected_types)} arguments, but got {len(args)}")

#         for arg, expected_type in zip(args, expected_types):
#             if not isinstance(arg, expected_type):
#                 raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

#     def generate_points(self):
#         """
#         Generates points for an epicycloid curve.

#         Returns:
#         Two arrays x and y containing the coordinates of the points.
#         """
#         t = np.linspace(0, 2 * np.pi, 1000)
#         x = (self.R + self.r) * np.cos(t) - self.d * np.cos((self.R + self.r) / self.r * t)
#         y = (self.R + self.r) * np.sin(t) - self.d * np.sin((self.R + self.r) / self.r * t)
#         return x, y


class ArchimedeanSpiral:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def check_args(self, *args):
        expected_types = [float, float]
        if len(args) != len(expected_types):
            raise ValueError(f"Expected {len(expected_types)} arguments, but got {len(args)}")
        for arg, expected_type in zip(args, expected_types):
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected {expected_type} but got {type(arg)} for argument {arg}")

    def generate_points(self):
        t = np.linspace(0, 10 * np.pi, 4000)
        r = self.a + self.b * t
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y

class CardioidCurve:
    def __init__(self, a: float):
        self.a = a

    def check_args(self, *args):
        expected_types = [float]
        if len(args) != 1:
            raise ValueError(f"Expected 1 argument, but got {len(args)}")
        if not isinstance(args[0], expected_types[0]):
            raise ValueError(f"Expected {expected_types[0]} but got {type(args[0])} for argument {args[0]}")

    def generate_points(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = self.a * (1 - np.cos(t)) * np.cos(t)
        y = self.a * (1 - np.cos(t)) * np.sin(t)
        return x, y

# class WattsCurve:
#     def __init__(self, a: float, b: float, c: float):
#         self.a = a
#         self.b = b
#         self.c = c
        

#     def generate_points(self):
#         t = np.linspace(0, 2 * np.pi, 1000)
#         cos_term = np.cos(t)
#         sin_term = np.sin(t)
#         sqrt_term = np.sqrt(self.c**2 - self.a**2 * cos_term**2)
        
#         x_plus = self.a * sin_term + sqrt_term
#         x_minus = self.a * sin_term - sqrt_term
        
#         # Calculate r avoiding invalid sqrt
#         r_plus = np.sqrt(np.maximum(self.b**2 - x_plus**2, 0))
#         r_minus = np.sqrt(np.maximum(self.b**2 - x_minus**2, 0))
        
#         # Combine both parts of the curve
#         x = np.concatenate((r_plus * cos_term, r_minus * cos_term[::-1]))
#         y = np.concatenate((r_plus * sin_term, -r_minus * sin_term[::-1]))
        
#         return x, y