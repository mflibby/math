import numpy as np


class DimError(Exception):
    pass

class DimError(Exception):
    pass

class DimError(Exception):
    pass

class Matrix():


    def __init__(self,obj):
        self.obj = obj
        self.T = self.transpose
        self.dim = (len(self.obj),len(self.obj[0]))
    ##########################
    def __iter__(self):
        self.i = 0
        self.j = 0
        self.curr= self.obj[self.i][self.j]
        return self
    #----------------------------
    def __next__(self):
        if (self.j == dim[0]):
            self.j =0
            self.i+=1
        try:
            self.curr = self.obj[self.i][self.j]
            self.j+=1
            return self.curr
        except:
            raise StopIteration
    #-----------------------------
    def __str__(self):
        temp = ""
        for i in self.obj:
            temp += str(i) + "\n"
        return temp
        #return str(self.obj)
    #-----------------------------
    def __getitem__(self,i):
        return self.obj[i]

    def _det(self, matrix):
        """
        Subfunction for self.det()
        """
        if (matrix.dim[0] != matrix.dim[1]):
            print(matrix.dim[0], ", ", matrix.dim[1])
            raise DimError("A matrix must be square in order for a determinant to exist")
        if (matrix.dim == (2,2)) :
            return matrix.obj[0][0]*matrix.obj[1][1]-matrix.obj[0][1]*matrix.obj[1][0]

        sub_det = []

        for i in range(matrix.dim[0]):
            sub_det.append(matrix._det(matrix._delete(matrix.delete(0,0),i,1)))
            sub_det[i] *= ((-matrix.obj[0][i])**(i))
        return sum(sub_det)
    def _delete(self,matrix,index, axis):
        if (axis == 0):
            temp = matrix.copy()
            del temp[index]
            return Matrix(temp)
        else:
            temp = Matrix(matrix.copy()).T()
            temp = temp.delete(index,0)
            return temp.T()
    ###########################
    # USER FUNCTIONS
    ###########################
    def transpose(self):
        return Matrix([[self.obj[j][i] for j in range(len(self.obj))] for i in range(len(self.obj[0]))])
    #-------------------------------------
    def det(self):
        """
        Takes a square matrix and returns the determinant
        """
        if (self.dim[0] != self.dim[1]):
            print(self.dim[0], ", ", self.dim[1])
            raise DimError("A matrix must be square in order for a determinant to exist")
        if (self.dim == (2,2)) :
            return self.obj[0][0]*self.obj[1][1]-self.obj[0][1]*self.obj[1][0]

        sub_det = []

        for i in range(self.dim[0]):
            sub_det.append(self._det(self._delete(self.delete(0,0),i,1)))
            sub_det[i] *= ((-self.obj[0][i])**(i))
        return sum(sub_det)

    def delete(self, index, axis):
        if (axis == 0):
            temp = self.obj.copy()
            del temp[index]
            return Matrix(temp)
        else:
            temp = Matrix(self.obj.copy()).T()
            temp.delete(index,0)
            return temp.T()

    def copy(self):
        """
        Returns a shallow copy of the matrix
        """
        return self.obj.copy()

def ip(a,b):
    """
    Takes matrices and returns their inner product
    """

    return sum([a[i][j]*b[i][j] for i in range(a.dim[0]) for j in range(b.dim[1])])

x = np.array([[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,1]])

y = np.array([[1,0],
              [0,1]])
