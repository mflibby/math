from integration import integrate
import numpy as np
y = lambda x: x**2
#area_func = lambda function,x,Δx : (function(x)+function(x+Δx))*Δx/2
integrate(y,[0,2])
x = np.arange(0,5,1)
Δx = 0.001
#x**2 * Δx
y(x)
