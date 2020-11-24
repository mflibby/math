from integration import *


e = 2.71828182845904523536
π = 3.1415926535897932384626433

def gamma(z):
    Γ = lambda x : x**(z-1)*e**(-x)
    return integrate(Γ, [0,100])


#def bessel(x, order = 1)
