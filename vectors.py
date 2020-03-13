
def cross_product(A,B):
    import numpy as np
        return np.array([A[1]*B[2]-A[2]*B[3], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0]])
