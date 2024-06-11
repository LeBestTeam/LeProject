import numpy as np
import matplotlib.pyplot as plt

class MatrixFractal:
    def __init__(self):
        # self.fractal_change_array = fractal_change_coefs
        pass

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
        for it in range(iterations):
            matrix = np.array([[0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                            [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix]])
            if it >= 1:
                if it == 1:
                    temp = matrix.reshape(matrix.shape[:-2])
                    temp = redo_array(temp)
                else:
                    temp = redo_array(matrix)

                matrix = temp
                temp = 1-temp
        plt.imshow(temp, cmap='gray')
        plt.show()

MatrixFractal().generate_points(2)


"""
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

def create_fractions(iterations):
    matrix = np.ones((1, 1))
    scale = 1
    fig, ax = plt.subplots(iterations+1, figsize=(20, 8*iterations))
    ax[0].imshow([matrix], cmap='gray')
    ax[0].set_title(f"Ітерація №{0}")
    for it in range(1, iterations+1):
        
        matrix = np.array([[0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [matrix, 0*matrix, matrix, 0*matrix, matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix], 
                           [0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix, 0*matrix]])
        # matrix = np.array([[matrix, matrix, matrix],
        #                    [matrix, 0*matrix, matrix],
        #                    [matrix, matrix, matrix]])
        if it >= 2:
            if it == 2:
                temp = matrix.reshape(matrix.shape[:-2])
                temp = redo_array(temp)
            else:
                temp = redo_array(matrix)
            
            matrix = temp
            temp = 1-temp
            ax[it].imshow(temp, cmap='gray')
            unique, counts = np.unique((1 - temp), return_counts=True)
            # dim = math.log(dict(zip(unique, counts))[1])/math.log(matrix.size)
            dim = math.log(dict(zip(unique, counts))[1], matrix.size)
            ax[it].set_title(f"Ітерація №{it}, fractal dim: {np.floor(dim)} <= {dim} <= {np.ceil(dim)}")
        else:
            matrix_to_show = 1-np.reshape(matrix, (matrix.shape[0]**it, matrix.shape[1]**it))
            ax[it].imshow(matrix_to_show, cmap='gray')
            unique, counts = np.unique((1 - matrix_to_show), return_counts=True)
            # dim = math.log(dict(zip(unique, counts))[1])/math.log(matrix.size)
            dim = math.log(dict(zip(unique, counts))[1], matrix.size)
            ax[it].set_title(f"Ітерація №{it}, fractal dim: {np.floor(dim)} <= {dim} <= {np.ceil(dim)}")
"""