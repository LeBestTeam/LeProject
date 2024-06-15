from Figures import LsystemFractal, AffineFractal, MatrixFractal, JuliaSet, MandelbrotSet, BrownianTree, BrownianMotion, NangularFractal
from Director import FigureDirector

import numpy as np


class App:
    def __init__(self):
        self.figures = {
            # Iteration Fractals
            "Lfractal": LsystemFractal.LsystemFractal,
            "Afractal": AffineFractal.AffineFractal,
            "Mfractal": MatrixFractal.MatrixFractal,
            # Complex Fractals
            "Juliafractal": JuliaSet.JuliaSet,
            "Mandelbrotfractal": MandelbrotSet.MandelbrotSet,
            # Random Fractals
            "BrownianTree": BrownianTree.BrownianTree,
            "BrownianMotion": BrownianMotion.BrownianMotion,
            "NangularFractal": NangularFractal.NangularFractal
        }

    def create_figure(self, name, *args, **kwargs):
        if name in self.figures:
            FigureDirector().build(self.figures[name](*args), **kwargs)
        else:
            raise ValueError("Wrong fractal name")


app = App()
app.create_figure("Lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 0., np.pi/2, it=5, animation_need=True, multi=200)
app.create_figure("Afractal", [
        [1.0, -0.1],
        [0.2, -1.0],
        [-0.3, 0.4],
        [0.7, 0.2],
        [0.5, -0.4],
        [-0.2, 0.5]
], it=4*10**4, animation_need=True, multi=200)

app.create_figure("Mfractal", np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), it=5, is_matrix=True, animation_need=True, interval=22)

app.create_figure("Juliafractal", complex(-0.4, 0.6), 2.0, 1000, 1000, it=100)
app.create_figure("Mandelbrotfractal", 2.0, 1000, 1000, it=100)

app.create_figure("BrownianTree", False, it=30, is_matrix=True, animation_need=True)
app.create_figure("BrownianMotion", 300, it=30000, is_matrix=True, animation_need=True)
app.create_figure("NangularFractal", np.array([
    [0, 0],
    [1, 5],
    [2, -1],
]), it=4*10**4, animation_need=True, multi=200)
