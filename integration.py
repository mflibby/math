def integrate(function,bounds,Δx=0.0001,area_func= lambda function, x, Δx : function(x)*Δx ):
    """
    Calculates the integral of an arbitrary function numerically using an arbitrary area function (the area function defaults to a basic
    rectangular area, with no preference to circumscribing vs inscribing)

    INPUTS:
    function  - like y = lambda x : x**2
    bounds    - 1D array with 2 elements, like [-5,100]
    Δx        - step size (i.e. width of areas). must be scalar
    area_func - could be a function of any kind, but must be prepared to deal with array multiplication like Δx*(np.arange(0,10,1)**2)

    RETURNS:
    area - area of the integral
    """
    import numpy as np
    return sum(area_func(function, np.arange(bounds[0],bounds[1],Δx), Δx))


def trap_integrate(function,bounds,Δx = 0.0001):
    """
    Calculates the integral of an arbitrary function numerically using a trapezoidal area, implementing the integrate function

    INPUTS:
    function  - like y = lambda x : x**2
    bounds    - 1D array with 2 elements, like [-5,100]
    Δx        - step size (i.e. width of areas). must be scalar

    RETURNS:
    area - area of the integral
    """
    return integrate(function,bounds,Δx,lambda function, x, Δx: (function(x)+function(x+Δx))*Δx*0.5)


class optimizeIntegral():
    """
    Use dynamic step size to ensure numerical integration has minimal eroneous values due to x-axis area cross over.

    INPUTS:
    function  - like y = lambda x : x**2
    bounds    - 1D array with 2 elements, like [-5,100]
    Δx        - step size (i.e. width of areas). must be scalar
    area_func - could be a function of any kind, but must be prepared to deal with array multiplication like Δx*(np.arange(0,10,1)**2)

    RETURNS:
    area - area of the integral
    """
    import numpy as np
    def __init__(function, bounds, Δx , area_func = lambda function, x, Δx : function(x)*Δx):
        self.func      = function
        self.bounds    = bounds
        self.step      = Δx
        self.area_func = area_func


    def roughOptimum():
        """
        Chops off cross-over values.
        """
        step_list = np.arange(self.bounds[0],self.bound[1],self.step)
        areas = []
        for i in step_list:
            if abs(self.func(i)+self.func(i+self.step))>=abs(self.func(i)):
                areas.append(self.area_func(self.func,i,self.step))
        return sum(areas)
