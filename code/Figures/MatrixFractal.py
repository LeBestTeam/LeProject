import numpy as np


class MatrixFractal:
    """
    Matrix implementation of fractals (see compgraph MKR)
    """
    def __init__(self, coefs:np.ndarray, *args):
        """
        Initiates Matrix fractal with given coefs but before checks if parameters are correct

        # Parameters:
        coefs: np.ndarray (coefs of matrix which will be used in iterations)
        """
        if args != ():
            raise ValueError(f"Wrong number of arguments, {args} excess")
        self.list_to_check = [np.ndarray]
        self.check_args(coefs)

        self.coefs = coefs

    def check_args(self, *args):
        """
        Checks if parameters are correct

        if not - raises ValueError with appropriate message
        """
        for argument_index in range(len(args)):
            if type(args[argument_index]) is not self.list_to_check[argument_index]:
                raise ValueError(f"Wrong argument {args[argument_index]}, which is {type(args[argument_index])} type, expected {self.list_to_check[argument_index]} type")


    def generate_points(self, iterations=3):
        """
        Generates more and more big matrix fractal on each iteration

        # Updates:
        Matrix each iteration

        # Returns:
        (row ^ N, col ^ N) matrix that should be displayed as image (plt.imshow)
        """
        def redo_array(array, out_array=None, *args):
            """
            Makes array from array of arrays using recursion

            array like [
                [
                    [1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]
                ],

                [
                    [1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]
                ]
            ]
            turns into array like [
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1]
             ]
            """
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
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ])).generate_points(4), cmap='gray')
    plt.show()
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
