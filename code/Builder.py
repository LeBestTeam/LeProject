from Figures.Figure import Figure


class FigureBuilder:
    def build(self, figure: Figure, *args):
        return figure.generate_points(*args)
