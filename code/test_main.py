import unittest
import numpy as np

import io
import contextlib

from main import App


class TestApp(unittest.TestCase):
    def test_invalid_create_fractal(self):
        self.assertRaises(ValueError, App().create_fractal, "WrongFractalName")

    def test_valid_create_fractal(self):
        App().create_fractal("lfractal", "F+F+F+F", {"F": "F+F-F-F+F"}, 2, 0, np.pi/2, show=False)


if __name__ == "__main__":
    unittest.main()
