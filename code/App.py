from Figures import LsystemFractal, AffineFractal, MatrixFractal, CardioidCurve, ArchimedeanSpiral, MorphingFractal
from Director import FigureDirector


class App:
    def __init__(self):

        self.fractals_class = {
            "Lfractal": LsystemFractal.LsystemFractal,
            "Afractal": AffineFractal.AffineFractal,
            "Mfractal": MatrixFractal.MatrixFractal,
            "CardioidCurve": CardioidCurve.CardioidCurve,
            "ArchimedeanSpiral": ArchimedeanSpiral.ArchimedeanSpiral,
            "MorphingFractal": MorphingFractal.MorphingFractal 
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

app.create("MorphingFractal","Julia", complex(-0.4, 0.6), 100, 2.0, 1000, 1000)
app.create("MorphingFractal", "Mandelbrot", 100, 2.0, 1000, 1000)
app.create("MorphingFractal", "Multibrot", 3, 100, 2.0, 1000, 1000)  
app.create("MorphingFractal", "BurningShip", 100, 2.0, 1000, 1000)
app.create("MorphingFractal", "Tricorn", 100, 2.0, 1000, 1000)