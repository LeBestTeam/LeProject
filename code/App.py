from Figures import LsystemFractal, AffineFractal, MatrixFractal, JuliaSet, MandelbrotSet, BrownianTree, BrownianMotion, NangularFractal, ReguralPolygon, DefaultPolynomialFunction
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
            "NangularFractal": NangularFractal.NangularFractal,
            # Non Fractals
            "ReguralPolygon": ReguralPolygon.RegularPolygon,
            "DefaultPolynomialFunction": DefaultPolynomialFunction.DefaultPolynomialFunction,
        }

    def create_figure(self, name, *args, **kwargs):
        if name in self.figures:
            FigureDirector().build(self.figures[name](*args), **kwargs)
        else:
            raise ValueError("Wrong fractal name")


app = App()
app.create_figure("Lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 0., np.pi/2, it=5, animation_need=True, multi=200, animation_save=False)
app.create_figure("Afractal", [
        [1.0, -0.1],
        [0.2, -1.0],
        [-0.3, 0.4],
        [0.7, 0.2],
        [0.5, -0.4],
        [-0.2, 0.5]
], it=4*10**4, animation_need=True, multi=200, animation_save=False)

app.create_fractal("Afractal", [
    [0.0500, 0.0500, 0.6000, 0.5000, 0.5000, 0.5500],
    [0.6000, -0.5000, 0.5000, 0.4500, 0.5500, 0.4000],
    [0.0000, 0.0000, 0.6980, 0.3490, -0.5240, -0.6980],
    [0.0000, 0.0000, 0.6980, 0.3492, -0.5240, -0.6980],
    [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
    [0.0000, 1.0000, 0.6000, 1.1000, 1.0000, 0.7000],
], 0, False, it=4*10**4, animation_need=True, multi=200, animation_save=False)


app.create_figure("Mfractal", np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), it=8, is_matrix=True, animation_need=True, interval=22, animation_save=False)

app.create_figure("Juliafractal", complex(-0.4, 0.6), 2.0, 1000, 1000, it=100)
app.create_figure("Mandelbrotfractal", 2.0, 1000, 1000, it=100)

app.create_figure("BrownianTree", False, it=100, is_matrix=True, animation_need=True, animation_save=False)
app.create_figure("BrownianMotion", 300, it=30000, is_matrix=True, animation_need=True, animation_save=False)
app.create_figure("NangularFractal", np.array([
    [0, 0],
    [1, 5],
    [2, -1],
]), it=4*10**4, animation_need=True, multi=200, animation_save=False)
app.create_fractal("NangularFractal", np.array([
    [1, 0],
    [3, 0],
    [1, 5],
    [5, 5],
]), it=4*10**4, animation_need=True, multi=200, animation_save=False)

app.create_figure("ReguralPolygon", 3., 0.5, it=100, animation_need=True, multi=2, animation_save=False)
app.create_figure("DefaultPolynomialFunction", -10.0, 10.0, [0, 0, 0, 1], it=100, animation_need=True, multi=20, animation_save=False)
