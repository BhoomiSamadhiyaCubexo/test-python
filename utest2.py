import unittest

class MyTest(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 5, msg="Adding 2 and 2 should equal 4, not 5")

if __name__ == '__main__':
    unittest.main()