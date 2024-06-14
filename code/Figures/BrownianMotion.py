import numpy as np
import numba


class BrownianMotion:
    def __init__(self, size,*args):
        self.size = size

    def check_args(self, *args):
        pass

    def generate_points(self, iteration):
        
        @numba.njit()
        def checkAround(x, y, squareSize, matrix):
            """
            Checks if there is friend or exit from circle around point (x, y), if not, chooses random way to go

            # Returns:
            x - x coordinate,
            y - y coordinate,
            friend_found - if there is dot nearby,
            edge_near - if there is edge nearny,
            exit_from_circle - if it exited from circle
            """
            friend_found = False
            exit_from_circle = False
            edge_near = False

            if (x + 1) > squareSize - 1 or (x - 1) < 1 or (y + 1) > squareSize - 1 or (y - 1) < 1:
                edge_near = True

                variant = np.random.choice(np.array([0, 1, 2, 3]), 1)
                x, y = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)][variant[0]]

            return x, y, friend_found, edge_near, exit_from_circle
        
        matrix = np.zeros((self.size, self.size))
        np.random.seed()
        x = np.random.randint(0, self.size)
        y = np.random.randint(0, self.size)
        for i in range(iteration):
            

        return matrix
