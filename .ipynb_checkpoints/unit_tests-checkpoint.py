import integration as i
import numpy as np
import functions as func
import matplotlib.pyplot as plt
import linear_algebra as lin
#x**2 * Δx
#y(x)

#x = np.linspace(1,10,50)
#y = [func.gamma(i) for i in x]
#plt.plot(x,y)
#plt.show()
#print(func.gamma(9))
#x = [[1,2,0]]
#X = lin.Matrix(x)
#print(lin.ip(X,X))

#print(func.zeta(.5))

for i in range(0,10):
    print(func.zeta(complex(.5,i)))
