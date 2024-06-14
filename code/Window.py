import os

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Window:
    def draw(self, input_value, **kwargs):
        if "is_matrix" in kwargs and kwargs["is_matrix"]:
            if type(input_value) is not list:
                plt.imshow(input_value, cmap='gray')
            else:
                if "animation_need" in kwargs and kwargs["animation_need"]:
                    fig, ax = plt.subplots()

                    ax.imshow(input_value[0], cmap='gray')  # matrix

                    def update(frame):
                        ax.clear()
                        ax.imshow(input_value[frame], cmap='gray')

                    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(input_value), interval=30)
                    if "animation_save" in kwargs and kwargs["animation_save"]:
                        if not os.path.isdir("images"):
                            os.mkdir("images")
                        add_to_name = len(os.listdir("./images"))
                        ani.save("./images/matrix_" + str(add_to_name) + '.gif', writer=animation.PillowWriter(fps=15))
                else:
                    plt.imshow(input_value[-1], cmap='gray')
        elif isinstance(input_value, tuple):
            x, y = input_value
            if "is_edge" in kwargs and kwargs["is_edge"]:
                plt.plot(x, y)
            else:
                if "markersize" in kwargs:
                    plt.plot(x, y, marker='o', linestyle='', markersize=kwargs["markersize"])
                else:
                    plt.plot(x, y, marker='o', linestyle='', markersize=0.6)
        else:
            plt.imshow(input_value, cmap='hot', extent=[-2, 2, -2, 2], interpolation='nearest')
            plt.colorbar(label='Iterations')

        plt.show()
