import numpy as np
import matplotlib.pyplot as plt

class MatrixFractal:
    def __init__(self, coefs:np.ndarray):
        self.coefs = coefs

    def check_args(self, *args):
        pass

    def generate_points(self, iterations=3):
        def redo_array(array, out_array=None, *args):
            if len(array.shape) == 2:
                if out_array is None:
                    out_array = array
                    return out_array
                else:
                    return np.concatenate((out_array, array), axis=1)

            for i in range(array.shape[0]):
                if len(args) < 1 and out_array is None:
                    out_array = redo_array(array[i], out_array, *args, i)
                elif len(args) == 1:
                    out_array = redo_array(array[i], out_array, *args, i)
                else:
                    out_array = np.concatenate((out_array, redo_array(array[i], None, *args, i)), axis=0)
            return out_array
        
        matrix = np.ones((1, 1))
        result = matrix
        for it in range(iterations):
            matrix = np.array([[coef * matrix for coef in row] for row in self.coefs])
            if matrix.shape[:-2] == (1, 1):
                matrix = matrix.reshape(matrix.shape[:-2])
            matrix = redo_array(matrix)
            result = 1-matrix
        return result

if __name__ == '__main__':
    plt.imshow(MatrixFractal(np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])).generate_points(2), cmap='gray')
    plt.show()
