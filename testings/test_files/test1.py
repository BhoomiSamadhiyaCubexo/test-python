def square(x):
    """
    This function calculates square of entered number
    >>> square(2)
    4
    >>> square(5)
    25
    """
    
    return x*x

if __name__ == "__main__":
    import doctest
    doctest.testmod()