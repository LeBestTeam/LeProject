import matplotlib.pyplot as plt


class Window:
    def draw(self, input_value, **kwargs):
        if "is_matrix" in kwargs and kwargs["is_matrix"]:
            plt.imshow(input_value, cmap='gray')

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
