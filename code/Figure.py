class Figure:
    def __init__(self, *args):
        pass

    def generate_points(self, iteration: int = 1):
        pass


class LsystemBuilder(Figure):
    def __init__(self, axiom: str, rules: dict, fi: float, dfi: float, *args):
        super.__init__(self, *args)
        self.axiom = axiom
        self.rules = rules
        self.max_iterations = max_iterations
        self.fi = fi
        self.dfi = dfi

    def check_args(self):
        pass
        # перевірити аргументи, якщо все ок дозволити будування
    
    def build(self):
        figure = Figure()
        def function(*args):
            pass
        figure.generate_points = function
        return figure
        # побудувати фігуру
        

class Window:
    def draw(self, input_value):
        pass


class FigureDirector:
    def __init__(self):
        pass

    def build(self, figure: Figure, window: Window):
        pass

