from L_Fractal import *
import matplotlib.pyplot as plt

fractal_board_builder = LFractalBuilder("F+F+F+F",{"F": "FF+F+F+F+FF"}, 0, 90)
fractal_board = fractal_board_builder.get_figure()


def draw(input_value, **kwargs): # from /Window.py
    # fig, ax = plt.subplots()
    # print(input_value)

    x, y = input_value

    if "is_edge" in kwargs and kwargs["is_edge"]:
        plt.plot(x, y)
    else:
        if "markersize" in kwargs:
            plt.plot(x, y, markersize=kwargs["markersize"])
        else:
            plt.plot(x, y, markersize=0.6)

    plt.show()

draw(fractal_board.generate_points(2))