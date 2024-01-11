import unittest

def add_product(cart, product, quantity):
    product_id, price = product
    if product_id in cart:
        cart[product_id] = (price, cart[product_id][1] + quantity)
    else:
        cart[product_id] = (price, quantity)
    return cart


def total_price(cart):
    return float(sum(price * quan for product_id, (price,quan) in cart.items()))

class TestECommerce(unittest.TestCase):

    def test_add_product(self):
        cart = {}
        cart = add_product(cart, ('P001', 100), 2)
        self.assertEqual(cart, {'P001': (100, 2)})
        cart = add_product(cart, ('P002', 200), 3)
        self.assertEqual(cart, {'P001': (100, 2), 'P002': (200, 3)})

    def test_calculate_total(self):
        cart = {'P001': (100, 2), 'P002': (200, 3)}
        total = total_price(cart)
        self.assertEqual(total, 800)

if __name__ == '__main__':
    unittest.main()