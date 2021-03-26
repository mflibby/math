from integration import *


e = 2.71828182845904523536
π = 3.1415926535897932384626433

def gamma(z):
    Γ = lambda x : x**(z-1)*e**(-x)
    return integrate(Γ, [0,100])


def zeta(s, max = 1000000):
    """
    Riemanns Zeta function - takes a complex argument s (and an optional integer argument 'max') and calculates the sum:
        ζ(s)=∑_{n=1}^{∞} \frac{1}{n^{s}}
    """
    temp = 0
    for i in range(1,max+1):
        temp += 1/(i**(s))
    return temp
#def bessel(x, order = 1)
