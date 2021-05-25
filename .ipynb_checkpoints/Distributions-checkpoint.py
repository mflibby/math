class Distribution:
    
    def __init__(self):
        self.e = 2.718281828459045235360287471352
    
class Discrete_Distribution(Distribution):
    pass
    
    
class Continuous_Distribution(Distribution):
    pass

##############################################

class Weibull_Distribution(Continuous_Distribution):
    
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        
        self.pdf = lambda x : (alpha/(beta**alpha))*(x**(alpha-1))*self.e**(-(x/beta)**alpha)
        self.cdf = lambda x : 1-self.e**(-(x/beta)**alpha)
        
    def p(self,X, left = True):
        if (type(X) is not list):
            return self.cdf(X) if left else 1-self.cdf(X)
        return self.cdf(X[1])-self.cdf(X[0])
    
    def point_perc(self,percent):
        return self.beta*(-np.log(1-percent))**(1/self.alpha)
    
    
class Gamma_Distribution(Continuous_Distribution):
    
    def __init__(self,alpha,beta=1):
        self.alpha = alpha
        self.beta = beta
        self.e = 2.718281828459045235360287471352
        self.pdf = lambda x : (1/( (beta**alpha) * gamma(alpha) ))*x**(alpha-1)*self.e**(-x/beta)
        self.cdf = lambda x, n : integrate(self.pdf,[0,n])

#TODO:
class ChiSquared_Distribution(Continuous_Distribution):
    pass

class Lognormal_Distribution(Continuous_Distribution):
    pass

class Beta_Distribution(Continuous_Distribution):
    pass

class Exponential_Distribution(Continuous_Distribution):
    pass

class Normal_Distribution(Continuous_Distribution):
    pass

class Uniform_Distribution(Continuous_Distribution):
    pass

###################################

class Poisson_Distribution(Discrete_Distribution):
    pass

class Binomial_Distribution(Discrete_Distribution):
    pass