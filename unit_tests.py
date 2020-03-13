import integration as i
import numpy as np

#x**2 * Δx
#y(x)


y = lambda x: np.sin(x**2)/np.log(x)
#i.trap_integrate(y,[0,2])

integral = i.optimizeIntegral(y,[1.1,10.1],0.00001, lambda function, x, Δx : .5*(function(x)+function(x+Δx))*Δx)
print('Dynamic Optimum: ', integral.dynamicOptimum(), '\nRough Optimum: ', integral.roughOptimum())
