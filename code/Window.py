import matplotlib.pyplot as plt


class Window:
    def draw(self, input_value, **kwargs):
        
        if isinstance(input_value, tuple):
            x, y = input_value
            if "is_edge" in kwargs and kwargs["is_edge"]:
                plt.plot(x, y)
            else:
                plt.plot(x, y, marker='o', linestyle='', markersize=0.6)
        else:
            plt.imshow(input_value, cmap='hot', extent=[-2, 2, -2, 2], interpolation='nearest')
            plt.colorbar(label='Iterations')
            
        plt.show()




