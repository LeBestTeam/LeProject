from Figures import LsystemFractal, AffineFractal, MatrixFractal
from Director import FigureDirector

import numpy as np


class App:
    def __init__(self):
        self.fractals_class = {
            "Lfractal": LsystemFractal.LsystemFractal,
            "Afractal": AffineFractal.AffineFractal,
            "Mfractal": MatrixFractal.MatrixFractal
        }

    def create_fractal(self, name, *args, **kwargs):
        if name in self.fractals_class:
            FigureDirector().build(self.fractals_class[name](*args), **kwargs)
        else:
            raise ValueError("Wrong fractal name")


app = App()
app.create_fractal("Lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 5, 0., np.pi/2)
app.create_fractal("Afractal", [
        [1.0, -0.1],
        [0.2, -1.0],
        [-0.3, 0.4],
        [0.7, 0.2],
        [0.5, -0.4],
        [-0.2, 0.5]
])
app.create_fractal("Mfractal", np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), it=2, is_matrix=True)
