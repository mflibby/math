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
