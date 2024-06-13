import numpy as np

import matplotlib.pyplot as plt

import numba


class BrownianTree:
    def __init__(self, print_need=False):
        self.print_need = print_need

    def generate_points(self, iteration):
        @numba.njit()
        def create_circle(matrix, x_limit, y_limit, radius, squareSize):
            for row in range(squareSize):
                for col in range(squareSize):

                    if row == x_limit and col == y_limit:
                        matrix[row, col] = 1

                    elif np.sqrt((x_limit-row)**2 + (y_limit-col)**2) > radius:
                        matrix[row, col] = 2
            return matrix

        @numba.njit()
        def checkAround(x, y, squareSize, matrix):
            friend_found = False
            exit_from_circle = False
            edge_near = False

            if (x + 1) > squareSize - 1 or (x - 1) < 1 or (y + 1) > squareSize - 1 or (y - 1) < 1:
                edge_near = True

            if not edge_near:
                neighbor_down = matrix[x + 1, y]
                if neighbor_down == 1:
                    friend_found = True
                if neighbor_down == 2:
                    exit_from_circle = True

                neighbor_up = matrix[x - 1, y]
                if neighbor_up == 1:
                    friend_found = True
                if neighbor_up == 2:
                    exit_from_circle = True

                neighbor_right = matrix[x, y+1]
                if neighbor_right == 1:
                    friend_found = True
                if neighbor_right == 2:
                    exit_from_circle = True

                neighbor_left = matrix[x, y-1]
                if neighbor_left == 1:
                    friend_found = True
                if neighbor_left == 2:
                    exit_from_circle = True

            if not friend_found and not edge_near:
                variant = np.random.choice(np.array([0, 1, 2, 3]), 1)
                x, y = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)][variant[0]]

            return x, y, friend_found, edge_near, exit_from_circle

        radius = iteration
        x_limit = radius + 2
        y_limit = radius + 2
        squareSize = radius*2+5

        matrix = np.zeros((squareSize, squareSize))

        matrix = create_circle(matrix, x_limit, y_limit, radius, squareSize)


        rwalkers_count = 0
        rwalkers_count_stopped = 0

        is_completed = False

        matrixs_for_animation = []

        anim_matrix_range = np.arange(0, 40000, radius//3)

        while not is_completed:
            rwalkers_count += 1
            np.random.seed()

            theta = 2 * np.pi * np.random.random()

            x = int(radius * np.cos(theta)) + x_limit
            y = int(radius * np.sin(theta)) + y_limit

            friend_found = False
            edge_near = False

            while not friend_found and not edge_near:
                x_new, y_new, friend_found, edge_near, exit_from_circle = checkAround(x, y, squareSize, matrix)

                if friend_found:
                    matrix[x, y] = 1
                    rwalkers_count_stopped += 1
                    if rwalkers_count_stopped in anim_matrix_range:
                        if self.print_need:
                            print("Random dots used on the field:", rwalkers_count, "from which", rwalkers_count_stopped, "was drawn")
                        matrixs_for_animation.append(matrix.copy())

                else:
                    x, y = x_new, y_new

            if friend_found and exit_from_circle:
                if self.print_need:
                    print("Dots drawn in the field:", rwalkers_count_stopped)
                is_completed = True

        matrixs_for_animation.append(matrix.copy())
        return matrixs_for_animation


if __name__ == "__main__":
    plt.matshow(BrownianTree(print_need=True).generate_points(30)[-1])
    plt.show()
