def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    if y>=10:
        k=0
        while y:
            if y>=10:
                k=k+(y%10)
                y=y//10
            else:
                k=k+y
                return k
    else:
        k=y
    return k
        
            
            
        