from integration import *
import numpy as np

e = 2.71828182845904523536
π = 3.1415926535897932384626433
ϕ = 1.6180339887498948482

def gamma(z, top = 10):
    Γ = lambda x : x**(z-1)*e**(-x)
    return integrate(Γ, (10**-9,top))


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
def zeta_cont(s):
    return integrate()

def primality(n):
    for i in range(2,round(np.sqrt(n))+1):
        if (n%i == 0):
            return False
    return True

def totient(n):
    """
    Euler's Totient Function - takes an integer argument 'n' and returns the list of numbers upto 'n' which are prime relative to it
    (i.e. do not exactly divide 'n')
    """
    totives = []
    for i in range(1,n):
        if (n%i != 0):
            totives.append(i)
    return totives

def around(y,x, ϵ = 0.001):
    if y<x and y>x-ϵ:
        return True
    if y>x and y<x+ϵ:
        return True
    return False


def avg(x):
    return sum(x)/len(x)

def summation(func, integers):
    n = integers
    tot = 0
    for i in n:
        tot += func(i)

def binco(n, k):
    return fact(n)/(fact(k)*fact(n-k))

def fact(x):
    temp = 1
    for i in np.arange(1, x+1, dtype = 'complex128'):
        temp *= i
    return temp


def find_peaks(data, func_fit, ϵ):
    x = data[0]
    y = data[1]
    z = func_fit(x)
    peaks = []
    adj = False
    adj_start = 0
    for i in range(len(y)):
        if around(y[i],z[i],ϵ):
            peaks.append((i,y[i]))
    return pd.DataFrame(peaks)

ζlist = lambda x, n : [(1/(i**(x))) for i in n]
