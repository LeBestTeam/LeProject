from Figures.Figure import Figure


class FigureBuilder:
    def build(self, figure: Figure):
        return figure.generate_points()
