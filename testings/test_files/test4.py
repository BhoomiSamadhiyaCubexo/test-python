def add_product(cart, prod, quan):
    
    """
    This function adds product to the cart 

    cart: (dictionary)
    prod: product(tuple)
    quan: no. of items(integer)
    
    returns: updated cart (dictionary)

    >>> cart={}
    >>> add_product({}, ('p01',100),2)
    {'p01': (100, 2)}
    >>> add_product(cart,('p02',20),1)   #we can use cart or {} either.
    {'p02': (20, 1)}
    
    """

    product_id, price = prod
    if product_id in cart :
        cart[product_id] = (price, cart[product_id][1] + quan)
    else:
        cart[product_id] = (price,quan)
    return cart


def total_price(cart):
    """
    Calculates total price of items in the cart.

    cart(dictionary)
    Returns: total sum (float)

    >>> cart = {'p01': (100,2), 'p02': (20,1)}
    >>> total_price(cart)
    220.0
    
    """
    return float(sum(price * quan for product_id, (price,quan) in cart.items()))


if __name__ == "__main__":
    import doctest
    doctest.testmod()