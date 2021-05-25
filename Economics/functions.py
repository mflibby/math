


def simple_interest ( P , i , n ) -> float:
    """
    Calculates the simple interest over n periods of applied interest i, given a starting principle P.
    INPUT:
        P : numerical - the starting principle
        i : numerical - the interest rate
        n : int       - the number of periods the interest compounds
    RETURN:
        F : numerical - P(1+i*n), the future value of P given i and n.
    """
    return P * ( 1 + i * n )


def compound_worth ( O , i , n , forward = True ) -> float:
    """
    Calculates the worth of O at some other time, either a future worth (when forward == True, which gives O == P);
    else present worth - i.e. O == F.
    INPUT:
        O : numerical   - the worth at some time, P if forward is True, else F
        i : numerical   - the interest rate
        n : int         - the number of periods the interest compounds
        forward : bool  - the direction of worth to be calculated, defaults to True
    RETURN:
        Z : numerical - P(1+i)^n, the future value of P given i and n, when forward == True,
                        else F(1+i)^-n, giving the present worth, i.e. the principle P needed to obtain F given i and n.
    """
    return O * ( ( 1 + i ) ** n ) if forward else O * ( ( 1 + i ) ** ( -n ) )



def series_F ( O , i , n , forward = True ) -> float:
    """
    Calculates the worth of n 'payments' of O at some other time, either a future worth (when forward == True, which gives O == A, Z == F);
    else worth at time of 'payment' - i.e. O == F, Z == A.
    INPUT:
        O : numerical   - the known variable, either A - the regular payments if forward == True, else F - the future worth of those payments
        i : numerical   - the interest rate
        n : int         - the number of periods the interest compounds
        forward : bool  - the direction of worth to be calculated, defaults to True
    RETURN:
        Z : numerical - A(((1+i)^n-1)/i), the future value of n payments of A given i and n, when forward == True,
                        else F(i/( (1+i)^n-1 )), the value of each A (assuming constant A, effectively an average) at time of payment.
    """
    return O * ( ( ( 1 + i ) ** n - 1 ) / i ) if forward else O * ( i / ( ( 1 + i ) ** n - 1 ) )

def series_P ( O , i , n , forward = True ) -> float:
    """
    Calculates the worth of n 'payments' of O at some other time, either worth at time of 'payment' (when forward == True, which gives O == P, Z == A);
    else a present worth - i.e. O == A, Z == P.
    INPUT:
        O : numerical   - the known variable, either P - the present worth of the payments A if forward == True, else A - the worth of each payment at the time of payment
        i : numerical   - the interest rate
        n : int         - the number of periods the interest compounds
        forward : bool  - the direction of worth to be calculated, defaults to True
    RETURN:
        Z : numerical - P( ( i(1+i)^n ) / ( (1+i)^n - 1 ) ), the neccessary value of A - for instance the needed payments to recoup a loss P
                        else A( ( (1+i)^n - 1 )  / ( i(1+i)^n ) ), the present worth of payments A, for instance the loss that n payments of A could cover.
    """
    return O * ( ( i * ( 1 + i ) ** n ) / ( ( 1 + i ) ** n - 1 ) ) if forward else O * ( ( ( 1 + i ) ** n - 1 ) / ( i * ( 1 + i ) ** n ) )


def arith_grad_series ( O , i , n , forward = True ) -> float:
    """
    Calculates the worth of n 'payments' of O at some other time, either worth at time of 'payment' (when forward == True, which gives O == P, Z == A);
    else a present worth - i.e. O == A, Z == P.
    INPUT:
        O : numerical   - the known variable, either G - the gradient factor if forward == True, else A - the worth of each payment at the time of payment
        i : numerical   - the interest rate
        n : int         - the number of periods the interest compounds
        forward : bool  - the direction of worth to be calculated, defaults to True
    RETURN:
        Z : numerical - G(  ( 1 / i ) - n / ( ( 1 + i )^n - 1 )  ), the neccessary value of A
                        else A/(  ( 1 / i ) - n / ( ( 1 + i )^n - 1 )  ), the gradient value.
    """
    return O * (  ( 1 / i ) - n / ( ( 1 + i ) ** n - 1 )  ) if forward else O / (  ( 1 / i ) - n / ( ( 1 + i ) ** n - 1 )  )


def arith_grad_worth ( O , i , n , forward = True ) -> float:
    """
    Calculates the worth of n 'payments' of O at some other time, either worth at time of 'payment' (when forward == True, which gives O == P, Z == A);
    else a present worth - i.e. O == A, Z == P.
    INPUT:
        O : numerical   - the known variable, either G - the gradient factor if forward == True, else A - the worth of each payment at the time of payment
        i : numerical   - the interest rate
        n : int         - the number of periods the interest compounds
        forward : bool  - the direction of worth to be calculated, defaults to True
    RETURN:
        Z : numerical - G(  ( 1 / i ) - n / ( ( 1 + i )^n - 1 )  ), the neccessary value of A
                        else A/(  ( 1 / i ) - n / ( ( 1 + i )^n - 1 )  ), the gradient value.
    """
    return O * (  ( 1 / i ) - n / ( ( 1 + i ) ** n - 1 )  ) if forward else O / (  ( 1 / i ) - n / ( ( 1 + i ) ** n - 1 )  )
