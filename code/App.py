import Figure
from Director import FigureDirector

import numpy as np


class App:
    def __init__(self):
        self.fractals_class = {"Lfractal": Figure.LsystemFractal} #, "Afractal": Figure.AffineFractal, "Mfractal": Figure.MatrixFractal}

    def create_fractal(self, name, *args):
        if name in self.fractals_class:
            FigureDirector().build(self.fractals_class[name](*args))
        else:
            raise ValueError("Wrong fractal name")


app = App()
app.create_fractal("Lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 5, 0., np.pi/2)
