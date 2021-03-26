
def cross_product(A,B):
    import numpy as np
    return np.array([A[1]*B[2]-A[2]*B[3], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0]])


def normalize(vec):
    import numpy as np
    return np.sqrt(vec**2)/vec

def normalize2(vec1,vec2):
    vec3 = vec2-vec1
    return vec3/(np.sqrt(sum([i**2 for i in vec3])))
