import unittest

from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
     
    def test_default_product_weight(self):
        """test default prod weight being 20"""
        prod = Product('Test')
        self.assertEqual(prod.weight, 20)
        

class AcmeReportTests(unittest.TestCase):
    def test_if_30(self):
        """checking if there is really 30 items in each list"""
        a = generate_products()
        self.assertEqual(len(a[2]), 30)
    
    def test_legal_names(self):
        """making a cycle that will go from 0 to 30 and 
        divide couples of legal names on noun and adjective, 
        then compare each to the list of the legal names"""
        b = generate_products()
        for i in range(0, (len(b[0])-1)):
            splitted = b[0][i].split(" ")
            self.assertIn(splitted[0], ADJECTIVES)
            self.assertIn(splitted[1], NOUNS)

if __name__ == '__main__':
    unittest.main()
