import numpy as np
import matplotlib.pyplot as plt

class LissajousCurve:
    def __init__(self,  a: float, b: float, delta: float):
   
        self.a = a
        self.b = b
        self.delta = delta

    def generate_points(self):
        t = np.linspace(0, 2 * np.pi, 4000)
        x = self.a * np.sin(self.a * t + self.delta)
        y = self.b * np.sin(self.b * t)
        return x, y




# curve = LissajousCurve(a=1.0, b=2.0, delta=np.pi / 2)
# curve.draw()
# curve = LissajousCurve(a=3.0, b=2.0, delta=np.pi / 2)
# curve.draw()
# curve = LissajousCurve(a=3.0, b=4.0, delta=np.pi / 2)
# curve.draw()
# curve = LissajousCurve(a=5.0, b=4.0, delta=np.pi / 2)
# curve.draw()