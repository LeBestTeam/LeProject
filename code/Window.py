import matplotlib.pyplot as plt


class Window:
    def draw(self, input_value):
        # fig, ax = plt.subplots()
        x, y = input_value
        plt.plot(x, y)
        plt.show()
    # Dasha's work
