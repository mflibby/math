import numpy as np



def det(matrix):
    """
    Takes a square matrix and returns the determinant
    """
    dim = len(matrix)
    if (dim == 2) :
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    sub_det = []

    for i in range(dim):
        sub_det.append(det(np.delete(np.delete(matrix,0,0),i,1)))
        sub_det[i] *= ((-matrix[0][i])**(i))
    return sum(sub_det)



x = np.array([[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,1]])

y = np.array([[1,0],
              [0,1]])
