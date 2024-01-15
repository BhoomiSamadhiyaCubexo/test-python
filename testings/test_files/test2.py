def add(a,b):
    """
    This program adds to numbers and generate output 
    >>> add(5,6)
    11.0
    >>> add(2.1,3.4)
    5.5
    """

    return float(a+b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()