class Figure:
    def __init__(self, *args):
        self.check_args(args)
    def check_args(self):
        print("check args F")
    def generate_points(self):
        pass


class LsystemBuilder(Figure):
    def __init__(self, axiom: str, rules: dict, max_iterations: int, fi: float, dfi: float, *args):
        super.__init__(self, *args)
        self.axiom = axiom
        self.rules = rules
        self.max_iterations = max_iterations
        self.fi = fi
        self.dfi = dfi

    def check_args(self):
        print("check args B")
    
    def generate_points(self):
        

class Window:
    def draw(self, input_value):
        pass


class FigureDirector:
    def __init__(self):
        pass

    def build(self, figure: Figure, window: Window):
        pass

