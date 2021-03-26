import numpy as np


class DimError(Exception):
    pass

class Matrix():


    def __init__(self,obj):


        self.T = self.transpose
        if (type(obj[0]) != list):
            self.obj = [obj]
            self.dim = (1,len(obj))
        else:
            self.obj = obj
            self.dim = (len(self.obj),len(self.obj[0]))
    ##########################
    def __iter__(self):
        self.i = 0
        #self.j = 0
        self.curr= self.obj[self.i]
        return self
    #----------------------------
    def __next__(self):
        try:
            self.curr = self.obj[self.i]
            self.i+=1
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

    def __mul__(self, other):
        if (type(other) == int or type(other) == float):
            return Matrix([[other * i for i in self.obj[j]] for j in range(self.dim[0])])
        if (self.dim[1] != other.dim[0]):
            raise DimError(f"The left matrix must have the same number of columns as the right matrix has rows but they have dimension C:{self.dim[1]}, R:{other.dim[0]}.")
        return Matrix([[sum([self.obj[i][k]*other.obj[k][j] for k in range(other.dim[0])])
                                                        for j in range(other.dim[1])]
                                                            for i in range(self.dim[0])])

    def __rmul__(self, other):
        if (type(other) == int or type(other) == float or type(other) == complex):
            return Matrix([[other * i for i in self.obj[j]] for j in range(self.dim[0])])

        if (self.dim[1] != other.dim[0]):
            print(self.dim[0], ", ", other.dim[1])
            raise DimError(f"The left matrix must have the same number of columns as the right matrix has rows but they have dimension C:{self.dim[1]}, R:{other.dim[0]}.")
        return Matrix([[sum([self.obj[i][k]*other.obj[k][j] for k in range(other.dim[0])])
                                                        for j in range(other.dim[1])]
                                                            for i in range(self.dim[0])])

    def __pow__(self, other):
        temp = self.copy()
        for i in range(other-1):
            temp *= self
        return temp


    #############################
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
            temp = matrix.copy().T()
            temp = temp.delete(index,0)
            return temp.T()

    def _check_square(self,error_string = f"A matrix must be square in order to perform this action"):
        if (self.dim[0] != self.dim[1]):
            print(self.dim[0], ", ", self.dim[1])
            raise DimError(error_string)
            return
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
        self._check_square("A matrix must be square in order for a determinant to exist")
        if (self.dim == (2,2)) :
            return self.obj[0][0]*self.obj[1][1]-self.obj[0][1]*self.obj[1][0]
        sub_det = []
        for i in range(self.dim[0]):
            sub_det.append(self._det(self._delete(self.delete(0,0),i,1)))
            sub_det[i] *= ((-self.obj[0][i])**(i+2))
        return sum(sub_det)

    def delete(self, index, axis):
        if (axis == 0):
            temp = self.obj.copy()
            del temp[index]
            return Matrix(temp)
        else:
            temp = self.copy.T()
            return temp.delete(index,0).T()

    def copy(self):
        """
        Returns a shallow copy of the matrix
        """
        return Matrix(self.obj.copy())

    def minors(self):
        self._check_square("A matrix must be square in order for a matrix of minors to exist")
        if (self.dim[0] == 2):
            raise DimError(self,f"A matrix must have a square dimension greater than 2 to have minors - dimension of input: {self.dim}")
        return Matrix([[self._det(self._delete(self.delete(j,0),i,1))
                                            for i in range(self.dim[0])]
                                               for j in range(self.dim[0])])

    def cofactors(self):
        self._check_square("A matrix must be square in order for a matrix of cofactors to exist")
        minor = self.minors()
        for i in range(self.dim[0]):
            for j in range(self.dim[0]):
                minor[i][j] *= (-1)**(i+j)
        return minor

    def adj(self):
        """
        Returns the adjoint of a square matrix, which is defined as the tranpose of that matrix's cofactor matrix
        """
        return self.cofactors().T()

    def inv(self):
        """
        Returns the inverse of a square matrix A, defined as A^-1 = (1/det(A))*adj(A)
        """
        self._check_square()
        if (self.dim[0] == 2):
            return (1/self.det())*Matrix([[]])
        return (1/self.det())*(self.cofactors().T())

    def trace(self):
        """
        Returns the trace of a square matrix, defined as the sum of the diagonal elements.
        """
        self._check_square()
        return sum([self.obj[i][j] if i == j else 0 for i in range(self.dim[0]) for j in range(self.dim[1])])

    def conjugate(self):
        return Matrix([[j.conjugate() for j in i] for i in self.obj])

    def herm_conj(self):
        return Matrix(self.obj).transpose().conjugate()

    def pLatex(self, matrixType = "bmatrix" , withAlign = False):
        """
        Returns the LaTeX code, using the input environment type, defaults to bmatrix
        """
        string = ""
        if (withAlign):
            string+= "\t\\begin{align}\n\t\t"
        string += f"\\begin{{{matrixType}}}\n"
        for i in range(self.dim[0]):
            if (withAlign):
                string += "\t\t"
            string += "\t"
            for j in range(self.dim[1]):
                if (type(self.obj[i][j]) != str):
                    string += str(round(self.obj[i][j]))
                else :
                    string += str(self.obj[i][j])
                if (j != self.dim[1] - 1):
                    string += " & "
            if (i != self.dim[0] - 1):
                string += "\\\\\n"
            else:
                if (withAlign):
                    string += f"\n\t\t\\end{{{matrixType}}}\n\t\\end{{align}}"
                else:
                    string += f"\n\\end{{{matrixType}}}"
        return string

    def augmented(self,space):
        return Matrix([[self.obj[i][j] if j < self.dim[1] else space[j-1] for j in range(self.dim[1]+1)] for i in range(self.dim[0])])

    def row_reduce(self):
        temp = self.copy()
        for i in range(temp.dim[0]):
            if i== temp.dim[1]:
                continue
            for j in range(temp.dim[1]):
                if j<=i:
                    continue
                try:
                    temp.obj[j] = [((temp[j][k]-(temp[i][k]*temp[j][i])/(temp[i][i]))) for k in range(0,self.dim[1])]
                except:
                    continue
        temp.obj = [[temp[i][k]/temp[i][i] for k in range(0,self.dim[1])] for i in range(self.dim[0])]
        return temp
    def row_echelon(self):
        #perform normal row reduction
        temp = self.row_reduce()

        #complete echelon reduction
        for i in range(temp.dim[0]):
            for j in range(0,i):
                temp.obj[j] = [temp[j][k] - temp[i][k]*(temp[j][i]/temp[i][i]) for k in range(0,self.dim[1])]

        #normalize rows
        temp.obj = [[temp[i][k]/temp[i][i] for k in range(0,self.dim[1])] for i in range(self.dim[0])]
        return temp

    def solve(self, space):
        temp = self.augmented(space)

        return

    def null_space(self):

        return


def zeros(shape):
    """
    Returns a list of zeros with the specified shape
    """
    return [0 for i in shape]

def ip(a,b):
    """
    Takes matrices and returns their inner product
    """

    return sum([a[i][j]*b[i][j] for i in range(a.dim[0]) for j in range(b.dim[1])])

def Ident(degree):
    """
    Creates an indentity matrix of the requested degree
    """
    return Matrix([[1 if i == j else 0 for i in range(degree)] for j in range(degree)])
x = [[1,1,0,2],
     [2,1,1,1],
     [1,3,1,0]]

y = [[-1,0],
     [0,1],
     [2,4]]

#print(Matrix(x).row_reduce().row_echelon()[:])
