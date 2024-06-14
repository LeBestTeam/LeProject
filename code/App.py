from Figures import LsystemFractal, AffineFractal, MatrixFractal, JuliaSet, MandelbrotSet, NEW_F, Lines
from Director import FigureDirector


class App:
    def __init__(self):

        self.fractals_class = {
            "Lfractal": LsystemFractal.LsystemFractal,
            "Afractal": AffineFractal.AffineFractal,
            "Mfractal": MatrixFractal.MatrixFractal,
            "Juliafractal": JuliaSet.JuliaSet,
            "Mandelbrotfractal": MandelbrotSet.MandelbrotSet,
            "CardioidCurve": Lines.CardioidCurve,
            "ArchimedeanSpiral": Lines.ArchimedeanSpiral,
            "BurningShipFractal": NEW_F.BurningShipFractal,
            "MultibrotFractal": NEW_F.MultibrotFractal,
            "TricornFractal": NEW_F.TricornFractal
        }


    def create(self, name, *args, **kwargs):
        if name in self.fractals_class:
            FigureDirector().build(self.fractals_class[name](*args), **kwargs)
        else:
            raise ValueError("Wrong fractal name")


app = App()

# app.create_fractal("Lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 5, 0., np.pi/2)
# app.create_fractal("Afractal", [
#         [1.0, -0.1],
#         [0.2, -1.0],
#         [-0.3, 0.4],
#         [0.7, 0.2],
#         [0.5, -0.4],
#         [-0.2, 0.5]
# ])

# app.create_fractal("Mfractal", np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), it=2, is_matrix=True)

# app.create_fractal("Juliafractal", complex(-0.4, 0.6), 100, 2.0, 1000, 1000)
# app.create_fractal("Mandelbrotfractal", 100, 2.0, 1000, 1000)

app.create("ArchimedeanSpiral", 0.5, 0.2)
app.create("CardioidCurve", 1.0)
app.create("BurningShipFractal", 100, 2.0, 1000, 1000)
app.create("MultibrotFractal", 3, 100, 2.0, 1000, 1000)
app.create("TricornFractal", 100, 2.0, 1000, 1000)