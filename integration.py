def integrate(function,bounds,Δx=0.0001,area_func= lambda function, x, Δx : function(x)*Δx ):
    import numpy as np
    area = 0
    x_list = np.arange(bounds[0],bounds[1],Δx)

    area = area_func(function,x,Δx)
    #for i in x_list:
    #    try:
    #        area += area_func(function,i,Δx)
    #    except:
    #        print('something went wrong...')
    return area
