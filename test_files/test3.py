def greet(yourname="Bhoomi"):
    """
    This program generates a greeting message
    example:
    >>> greet()
    Hello,Bhoomi! Nice to meet you.
    >>> greet("Joker")
    Hello,Joker! Nice to meet you.
    """
    print(f"Hello,{yourname}! Nice to meet you.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    