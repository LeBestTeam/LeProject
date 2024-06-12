import Figure
from Director import FigureDirector

import numpy as np


class App:
    def __init__(self):
        self.fractals_class = {"Lfractal": Figure.LsystemFractal, 
                               "Afractal": Figure.AffineFractal, 
                               "Juliafractal": Figure.JuliaSet,
                               "Mandelbrotfractal": Figure.MandelbrotSet}#, "Mfractal": Figure.MatrixFractal}

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

app.create_fractal("Juliafractal", complex(-0.4, 0.6), 100, 2.0, 1000, 1000)
app.create_fractal("Mandelbrotfractal", 100, 2.0, 1000, 1000)
