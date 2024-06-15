from Figures import LsystemFractal, AffineFractal, MatrixFractal, CardioidCurve, ArchimedeanSpiral, LissajousCurve, MorphingFractal, BrownianTree,BrownianTree, NangularFractal, BrownianMotion
from Director import FigureDirector

import numpy as np

class App:
    def __init__(self):

        self.fractals_class = {
            # Iteration Fractals
            "Lfractal": LsystemFractal.LsystemFractal,
            "Afractal": AffineFractal.AffineFractal,
            "Mfractal": MatrixFractal.MatrixFractal,
            "CardioidCurve": CardioidCurve.CardioidCurve,
            "ArchimedeanSpiral": ArchimedeanSpiral.ArchimedeanSpiral,
            "MorphingFractal": MorphingFractal.MorphingFractal,
            # "LissajousCurve": LissajousCurve.LissajousCurve,
            # "BrownianTree": BrownianTree.BrownianTree,
            # "BrownianMotion": BrownianMotion.BrownianTree,
            # "NangularFractal": NangularFractal.NangularFractal
        }


    def create(self, name, *args, **kwargs):
        if name in self.fractals_class:
            FigureDirector().build(self.fractals_class[name](*args), **kwargs)
        else:
            raise ValueError("Wrong name")


app = App()
app.create_fractal("Lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 5, 0., np.pi/2)
app.create_fractal("Afractal", [
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


app.create_fractal("Mfractal", np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), it=8, is_matrix=True, animation_need=True, interval=22, animation_save=False)



app.create_fractal("BrownianTree", False, it=100, is_matrix=True, animation_need=True, animation_save=False)
app.create_fractal("BrownianMotion", 300, it=30000, is_matrix=True, animation_need=True, animation_save=False)
app.create_fractal("NangularFractal", np.array([
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

app.create_fractal("Juliafractal", complex(-0.4, 0.6), 100, 2.0, 1000, 1000)
app.create_fractal("Mandelbrotfractal", 100, 2.0, 1000, 1000)

app.create("ArchimedeanSpiral", 0.5, 0.2)
app.create("CardioidCurve", 1.0)
app.create("LissajousCurve", 1.0, 2.0, np.pi/2)
app.create("LissajousCurve", 3.0, 2.0, np.pi/2)
app.create("LissajousCurve", 3.0, 4.0, np.pi/2)
app.create("LissajousCurve", 5.0, 4.0, np.pi/2)


app.create("MorphingFractal","Julia", complex(-0.4, 0.6), 100, 2.0, 1000, 1000)
app.create("MorphingFractal", "Mandelbrot", 100, 2.0, 1000, 1000)
app.create("MorphingFractal", "Multibrot", 3, 100, 2.0, 1000, 1000)  
app.create("MorphingFractal", "BurningShip", 100, 2.0, 1000, 1000)
app.create("MorphingFractal", "Tricorn", 100, 2.0, 1000, 1000)