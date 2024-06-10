from Builder import FigureBuilder
from Figure import Figure
from Window import Window


class FigureDirector:
    def build(self, figure: Figure, *args, **kwargs):
        Window().draw(FigureBuilder().build(figure, *args, **kwargs))
