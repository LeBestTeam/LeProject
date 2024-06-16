import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Window:
    def draw(self, input_value, **kwargs):
        multiplayer = 1
        if "multiplayer" in kwargs:
            if isinstance(kwargs["multiplayer"], (int, float)):
                multiplayer = kwargs["multiplayer"]
        if "multi" in kwargs:
            if isinstance(kwargs["multi"], (int, float)):
                multiplayer = kwargs["multi"]

        interval = 1
        if "interval" in kwargs:
            if isinstance(kwargs["interval"], (int, float)):
                interval = kwargs["interval"]

        if "animation_save" in kwargs and kwargs["animation_save"]:
            if not os.path.isdir("images"):
                os.mkdir("images")
            add_to_name = len(os.listdir("./images"))

        if "is_matrix" in kwargs and kwargs["is_matrix"]:
            if isinstance(input_value, list):
                if "animation_need" in kwargs and kwargs["animation_need"]:
                    fig, ax = plt.subplots()

                    ax.imshow(input_value[0], cmap='gray')  # matrix

                    def update(frame):
                        ax.clear()
                        ax.imshow(input_value[frame], cmap='gray')

                    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(input_value), interval=30 * interval)
                    if "animation_save" in kwargs and kwargs["animation_save"]:
                        ani.save("./images/figure_" + str(add_to_name) + '.gif', writer=animation.PillowWriter(fps=15))
                else:
                    plt.imshow(input_value[-1], cmap='gray')
            else:
                plt.imshow(input_value, cmap='gray')

        elif isinstance(input_value, tuple):
            x, y = input_value
            if "is_edge" in kwargs and kwargs["is_edge"]:
                plt.plot(x, y)
            else:
                markersize = kwargs.get("markersize", 0.6)
                if "animation_need" in kwargs and kwargs["animation_need"]:
                    fig, ax = plt.subplots()

                    ax.plot(x, y, marker='o', linestyle='', markersize=markersize)

                    def update(frame):
                        frame = frame * multiplayer
                        ax.clear()
                        ax.plot(x[:frame], y[:frame], marker='o', linestyle='', markersize=markersize)

                    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(x) // multiplayer, interval=30 * interval)
                    if "animation_save" in kwargs and kwargs["animation_save"]:
                        ani.save("./images/figure_" + str(add_to_name) + '.gif', writer=animation.PillowWriter(fps=15))
                else:
                    plt.plot(x, y, marker='o', linestyle='', markersize=markersize)

        else:  
            fig, ax = plt.subplots(figsize=(8, 8))

            cmap = plt.get_cmap('inferno')

            frames = []

            max_iter = kwargs.get('max_iter', 100)

            for i in range(max_iter):
                frame = ax.imshow(input_value.T, cmap=cmap, vmin=0, vmax=max_iter)
                frame.set_clim(vmin=0, vmax=i)
                frames.append([frame])

            ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=1000)

            if kwargs.get('save_gif', False):
                filename = kwargs.get('filename', 'morphing.gif') # it saves fractal with its own name!! 
                filepath = os.path.join('./images', filename)
                writer = animation.PillowWriter(fps=30)
                ani.save(filepath, writer=writer)
            
            else:
                plt.show()


        plt.show()



''' my initial draw() for morhing fractals only (in case i incorectly merged it into Maks's code for draw()'''
    # def draw(self, iterations, max_iter=100, save_gif=False, filename='julia_set.gif'):
    #         fig, ax = plt.subplots(figsize=(8, 8))

    #         cmap = plt.get_cmap('inferno')

    #         frames = []

    #         for i in range(max_iter):
    #             frame = ax.imshow(iterations.T, cmap=cmap, vmin=0, vmax=max_iter)
    #             frame.set_clim(vmin=0, vmax=i)
    #             frames.append([frame])

    #         ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=1000)

    #         if save_gif:
    #             writer = animation.PillowWriter(fps=30)
    #             ani.save(filename, writer=writer)
    #         else:
    #             plt.show()