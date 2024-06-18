import numpy as np
import matplotlib.pyplot as plt


class BrownianMotion:
    def __init__(self, size: int, *args):
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [int]
        self.check_args(size)

        self.size = size

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")

    def generate_points(self, iteration):
        """
        Generates dot of brownian motion on each iteration

        # Returns:
        (size, size) matrix that should be displayed as image (plt.imshow)
        """
        def checkAround(x, y, size_limit):
            """
            Checks if there is friend or exit from circle around point (x, y), if not, chooses random way to go

            # Returns:
            x - x coordinate,
            y - y coordinate,
            """
            coefs = [0, 1, 2, 3]
            if x - 1 < 0:
                coefs.remove(0)
            if x + 1 > size_limit - 1:
                coefs.remove(1)
            if y - 1 < 0:
                coefs.remove(2)
            if y + 1 > size_limit - 1:
                coefs.remove(3)
            array = np.array([0, 1, 2, 3])
            variant = np.random.choice(array[coefs], 1)
            x, y = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)][variant[0]]

            return x, y

        matrix = np.zeros((self.size, self.size))
        matrix_for_animation = []

        np.random.seed()
        x = np.random.randint(0, self.size)
        y = np.random.randint(0, self.size)

        for i in range(iteration):
            matrix[x, y] = 1
            if i in np.arange(0, iteration, self.size//3):
                matrix_for_animation.append(matrix.copy())
            x, y = checkAround(x, y, self.size)

        matrix_for_animation.append(matrix.copy())
        return matrix_for_animation


if __name__ == "__main__":
    plt.imshow(BrownianMotion(100).generate_points(10000)[-1])
    plt.show()
