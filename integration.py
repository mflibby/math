def integrate(function,bounds,Δx=0.0001,area_func= lambda function, x, Δx : function(x)*Δx ):
    import numpy as np
    area = 0
    x_list = np.arange(bounds[0],bounds[1],Δx)
    for i in x_list:
        try:
            area += area_func(function,i,Δx)
        except:
            print('something went wrong...')
    return area

y = lambda x: x**2
integrate(y,[0,2],area_func = lambda function,x,Δx : (function(x)+function(x+Δx))*Δx/2)
