from Figures import (
    LsystemFractal, AffineFractal, MatrixFractal, CardioidCurve, ArchimedeanSpiral,
    LissajousCurve, MorphingFractal, BrownianTree, NangularFractal, BrownianMotion,
    RegularPolygon, DefaultPolynomialFunction
)
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
            "MorphingFractal": MorphingFractal.MorphingFractal,
            # Random Fractals
            "BrownianTree": BrownianTree.BrownianTree,
            "BrownianMotion": BrownianMotion.BrownianMotion,
            "NangularFractal": NangularFractal.NangularFractal,
            # Non Fractals
            "ReguralPolygon": RegularPolygon.RegularPolygon,
            "DefaultPolynomialFunction": DefaultPolynomialFunction.DefaultPolynomialFunction,
            "CardioidCurve": CardioidCurve.CardioidCurve,
            "ArchimedeanSpiral": ArchimedeanSpiral.ArchimedeanSpiral,
            "LissajousCurve": LissajousCurve.LissajousCurve,             
        }

    def create_figure(self, name, *args, **kwargs):
        if name in self.figures:
            FigureDirector().build(self.figures[name](*args), **kwargs)
    def create_figure(self, name, *args, **kwargs):
        if name in self.figures:
            FigureDirector().build(self.figures[name](*args), **kwargs)
        else:
            raise ValueError("Wrong fractal name")


if __name__ == "__main__":
    app = App()

    app.create_figure("Lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 0., np.pi/2,
                      it=5, animation_need=True, animation_save=False, multi=200, has_background=False, has_axes=False)
    app.create_figure("Afractal", [
                        [1.0, -0.1],
                        [0.2, -1.0],
                        [-0.3, 0.4],
                        [0.7, 0.2],
                        [0.5, -0.4],
                        [-0.2, 0.5]
                    ],
                      it=4*10**4, animation_need=True, animation_save=False, multi=200, has_background=False, has_axes=False)

    app.create_figure("Afractal", [
                        [0.0500, 0.0500, 0.6000, 0.5000, 0.5000, 0.5500],
                        [0.6000, -0.5000, 0.5000, 0.4500, 0.5500, 0.4000],
                        [0.0000, 0.0000, 0.6980, 0.3490, -0.5240, -0.6980],
                        [0.0000, 0.0000, 0.6980, 0.3492, -0.5240, -0.6980],
                        [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
                        [0.0000, 1.0000, 0.6000, 1.1000, 1.0000, 0.7000],
                    ], 0, False,
                      it=4*10**4, animation_need=True, animation_save=False, multi=200, has_background=False, has_axes=False)

    app.create_figure("Mfractal", np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]),
                      it=8, animation_need=True, animation_save=False, has_background=False, has_axes=False)

    app.create_figure("BrownianTree", False,
                      it=50, animation_need=True, animation_save=False, has_background=False, has_axes=False)
    app.create_figure("BrownianMotion", 300,
                      it=30000, animation_need=True, animation_save=False, has_background=False, has_axes=False)
    app.create_figure("NangularFractal", np.array([
                        [0, 0],
                        [1, 5],
                        [2, -1],
                    ]),
                      it=4*10**4, animation_need=True, animation_save=False, multi=200, has_background=False, has_axes=False)
    app.create_figure("NangularFractal", np.array([
                        [1, 0],
                        [3, 0],
                        [1, 5],
                        [5, 5],
                    ]),
                      it=4*10**4, animation_need=True, animation_save=False, multi=200, has_background=False, has_axes=False)

    app.create_figure("ReguralPolygon", 3., 0.5,
                      it=12, animation_need=True, animation_save=False, multi=1, fps=10, is_edge=True, is_fixed_size=True, has_background=False, has_axes=False)
    app.create_figure("DefaultPolynomialFunction", -10.0, 10.0, [0, 0, 0, 1],
                      it=1000, animation_need=True, animation_save=False, multi=200, is_fixed_size=True, has_background=False, has_axes=False)

    app.create_figure("ArchimedeanSpiral", 0.5, 0.2,
                      it=4000, animation_need=True, animation_save=False, multi=70, is_fixed_size=True, has_background=False, has_axes=False)
    app.create_figure("CardioidCurve", 1.0,
                      it=4000, animation_need=True, animation_save=False, multi=20, is_fixed_size=True, has_background=False, has_axes=False)
    app.create_figure("LissajousCurve", 1.0, 2.0, np.pi/2,
                      it=4000, animation_need=True, animation_save=False, multi=70, is_fixed_size=True, has_background=False, has_axes=False)
    app.create_figure("LissajousCurve", 3.0, 2.0, np.pi/2,
                      it=4000, animation_need=True, animation_save=False, multi=70, is_fixed_size=True, has_background=False, has_axes=False)
    app.create_figure("LissajousCurve", 3.0, 4.0, np.pi/2,
                      it=4000, animation_need=True, animation_save=False, multi=70, is_fixed_size=True, has_background=False, has_axes=False)
    app.create_figure("LissajousCurve", 5.0, 4.0, np.pi/2,
                      it=4000, animation_need=True, animation_save=False, multi=70, is_fixed_size=True, has_background=False, has_axes=False)

    app.create_figure("MorphingFractal", "Julia", complex(-0.4, 0.6), 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
    app.create_figure("MorphingFractal", "Julia", complex(0.4, 0.4), 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
    app.create_figure("MorphingFractal", "Mandelbrot", 100, 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
    app.create_figure("MorphingFractal", "Multibrot", 3, 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
    app.create_figure("MorphingFractal", "BurningShip", 100, 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
    app.create_figure("MorphingFractal", "Tricorn", 100, 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
    app.create_figure("MorphingFractal", "SinJulia", complex(-0.4, 0.6), 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
    app.create_figure('MorphingFractal', 'HyperbolicTangent', complex(0.1, 0.1), 2.0, 1000, 1000,
                      it=100, animation_need=True, animation_save=False, cmap='inferno', has_background=False, has_axes=False)
