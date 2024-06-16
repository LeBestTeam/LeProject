import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Window:
    def draw(self, input_value, **kwargs):
        multiplayer = kwargs.get("multiplayer", 1) * kwargs.get("multi", 1)
        interval = kwargs.get("interval", 30)
        markersize = kwargs.get("markersize", 0.6)
        figsize = kwargs.get("figsize", (5, 5))
        fps = kwargs.get("fps", 15)

        cmap = kwargs.get("cmap", 'gray')  # 'inferno'

        animation_need = kwargs.get("animation_need", False)
        animation_save = kwargs.get("animation_save", False)

        is_edge = kwargs.get("is_edge", False)
        is_fixed_size = kwargs.get("is_fixed_size", False)

        has_axes = kwargs.get("has_axes", True)
        has_background = kwargs.get("has_background", True)

        if animation_save:
            if not os.path.isdir("images"):
                os.mkdir("images")
            add_to_name = len(os.listdir("./images"))
            filename = kwargs.get('filename', 'figure' + str(add_to_name))

        try:
            x, y = input_value
            is_matrix = False
        except ValueError:
            is_matrix = True

        if is_matrix:
            if not isinstance(input_value, list):
                plt.imshow(input_value, cmap=cmap)
            elif not animation_need:
                plt.imshow(input_value[-1], cmap=cmap)
            else:
                fig, ax = plt.subplots(figsize=figsize, constrained_layout=(not has_background))

                ax.imshow(input_value[0], cmap=cmap)
                if not has_axes:
                    ax.axis('off')

                def update(frame):
                    ax.clear()
                    ax.imshow(input_value[frame], cmap=cmap)
                    if not has_axes:
                        ax.axis('off')

                ani = animation.FuncAnimation(fig=fig, func=update, frames=len(input_value), interval=interval)
        else:
            if is_fixed_size:
                x_limit_left = min(x) - abs(min(x)) / 2
                x_limit_right = max(x) + abs(max(x)) / 2
                y_limit_bottom = min(y) - abs(min(y)) / 2
                y_limit_top = max(y) + abs(max(y)) / 2
            if is_edge:
                plt.plot(x, y)
            else:
                if not animation_need:
                    plt.plot(x, y, marker='o', linestyle='', markersize=markersize)
                else:
                    fig, ax = plt.subplots(figsize=figsize, constrained_layout=(not has_background))

                    if is_fixed_size:
                        ax.set_xlim(x_limit_left, x_limit_right)
                        ax.set_ylim(y_limit_bottom, y_limit_top)
                    if not has_axes:
                        ax.axis('off')
                    ax.plot(x, y, marker='o', linestyle='', markersize=markersize)

                    def update(frame):
                        frame = frame * multiplayer
                        ax.clear()
                        if is_fixed_size:
                            ax.set_xlim(x_limit_left, x_limit_right)
                            ax.set_ylim(y_limit_bottom, y_limit_top)
                        if not has_axes:
                            ax.axis('off')
                        ax.plot(x[:frame], y[:frame], marker='o', linestyle='', markersize=markersize)

                    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(x)//multiplayer, interval=interval)

        if animation_need and animation_save:
            ani.save("./images/" + filename + '.gif', writer=animation.PillowWriter(fps=fps))

        plt.show()
