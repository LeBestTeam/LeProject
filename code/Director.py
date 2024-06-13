from Builder import FigureBuilder
from Figures.Figure import Figure
from Window import Window


class FigureDirector:
    def build(self, figure: Figure, **kwargs):
        if "it" in kwargs:
            Window().draw(FigureBuilder().build(figure, kwargs['it']), **kwargs)
        elif "iterations" in kwargs:
            Window().draw(FigureBuilder().build(figure, kwargs['iterations']), **kwargs)
        else:
            Window().draw(FigureBuilder().build(figure), **kwargs)
