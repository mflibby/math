from integration import integrate
import numpy as np

#x**2 * Δx
#y(x)


y = lambda x: x**2
integrate(y,[0,2],area_func = lambda function,x,Δx : (function(x)+function(x+Δx))*Δx/2)
