import numpy as np
import matplotlib.pyplot as plt


class NangularFractal:
    """
    Fractal that on start has n-dots, starts with random dot and goes on half of distance to randomly chosen dot given
    """
    def __init__(self, dots_array: np.ndarray, *args):
        """
        Initiates Nangular fractal with given parameters but before checks if parameters are correct

        # Parameters:
        dots_array: np.ndarray (starting n-dots of [x, y])
        """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [np.ndarray]
        self.check_args(dots_array)

        self.dots_array = dots_array
        self.result = dots_array.copy()

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")

        if args[0].shape[1] != 2:
            raise ValueError(f"Wrong shape of array {args[0]}, which is {args[0].shape} shape, expected (n, 2)")

    def generate_points(self, iteration):
        """
        Generates `iteration` number of dots
        # Returns:
        (iteration + 4, 2) arrays of x and y coordinates
        """
        x = np.random.randint(min(self.dots_array[:, 0]), max(self.dots_array[:, 0]))
        y = np.random.randint(min(self.dots_array[:, 1]), max(self.dots_array[:, 1]))

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
        [2, 0],
    ])).generate_points(4*10**4)
    plt.plot(x, y, marker='o', linestyle='', markersize=1)
    plt.show()
