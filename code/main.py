import numpy as np

import Fractals


class App:
    """
    Main bridge between user and drawings

    Use `create_fractal(name, *args)` to create fractals
    """
    def __init__(self):
        self.fractals = {"lfractal": Fractals.LFractal, "afractal": Fractals.AffineFractal, "mfractal": Fractals.MatrixFractal}

    def create_fractal(self, name, *args):
        """
        Checks if fractal name given exists and creates it
        """
        if name in self.fractals:
            return self.fractals[name](*args).build()
        else:
            raise ValueError("Wrong fractal name")


if __name__ == "__main__":
    app = App()
    app.create_fractal("lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 5, 0, np.pi/2)
    app.create_fractal("mfractal")
