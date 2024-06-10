import matplotlib.pyplot as plt


class Window:
    def draw(self, input_value, **kwargs):
        # fig, ax = plt.subplots()
        # print(input_value)

        x, y = input_value

        if "is_edge" in kwargs and kwargs["is_edge"]:
            plt.plot(x, y)
        else:
            if "markersize" in kwargs:
                plt.plot(x, y, marker='o', linestyle='', markersize=kwargs["markersize"])
            else:
                plt.plot(x, y, marker='o', linestyle='', markersize=0.6)

        plt.show()
    # Dasha's work
