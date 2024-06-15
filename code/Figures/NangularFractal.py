import numpy as np
import matplotlib.pyplot as plt


class NangularFractal:
    def __init__(self, dots_array: np.ndarray, *args):
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [np.ndarray]
        self.check_args(dots_array)

        self.dots_array = dots_array
        self.result = dots_array.copy()

    def check_args(self, *args):
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")

        # for parameter in args[0]:

    def generate_points(self, iteration):
        x = np.random.randint(0, max(self.dots_array[:, 0]))
        y = np.random.randint(0, max(self.dots_array[:, 1]))
        self.result = np.concatenate((self.result, np.array([[x, y]])))
        for i in range(iteration):
            random_dot = self.dots_array[np.random.choice(self.dots_array.shape[0], 1)][0]
            x = (x+random_dot[0]) / 2
            y = (y+random_dot[1]) / 2
            self.result = np.concatenate((self.result, np.array([[x, y]])))

        return self.result[:, 0], self.result[:, 1]


if __name__ == "__main__":
    x, y = NangularFractal(np.array([
        [0, 0],
        [1, 5],
        [2, -1],
    ])).generate_points(4*10**4)
    plt.plot(x, y, marker='o', linestyle='', markersize=1)
    plt.show()
