import numpy as np

import Fractals


class App:
    """
    Main bridge between user and drawings

    Use `create_fractal(name, *args)` to create fractals
    """
    def __init__(self):
        self.fractals = {"lfractal": Fractals.LFractal, "afractal": Fractals.AffineFractal, "mfractal": Fractals.MatrixFractal}

    def create_fractal(self, name, *args, **kwargs):
        """
        Checks if fractal name given exists and creates it

        # Available fractals:
        `lfractal`, `afractal`, `mfractal`
        """
        if name in self.fractals:
            return self.fractals[name](*args).build(**kwargs)
        else:
            raise ValueError("Wrong fractal name")


if __name__ == "__main__": # pragma: no cover
    app = App()
    app.create_fractal("lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 5, 0, np.pi/2)
    app.create_fractal("afractal", [
        [1.0, -0.1],
        [0.2, -1.0],
        [-0.3, 0.4],
        [0.7, 0.2],
        [0.5, -0.4],
        [-0.2, 0.5]
])
