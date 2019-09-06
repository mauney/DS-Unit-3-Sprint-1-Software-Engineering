#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


# def setUp(self):
#     self.prod = Product('Test Product')


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_default_product_identifier(self):
        """Test default product identifier being 7 digits."""
        prod = Product('Test Product')
        self.assertIn(prod.identifier, range(1000000, 10000000))

    def test_stealability_and_explode(self):
        """Test stealability and explode with non-default inputs"""
        prod_low = Product('low_risk', price=1, weight=4, flammability=1)
        self.assertEqual(prod_low.stealability(), 'Not so stealable...')
        self.assertEqual(prod_low.explode(), '...fizzle.')

        prod_med = Product('med_risk', price=3, weight=4, flammability=3)
        self.assertEqual(prod_med.stealability(), 'Kinda stealable.')
        self.assertEqual(prod_med.explode(), '...boom!')

        prod_high = Product('high_risk', price=5, weight=4, flammability=20)
        self.assertEqual(prod_high.stealability(), 'Very stealable!')
        self.assertEqual(prod_high.explode(), '...BABOOM!')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_default_num_products(self):
        """Test that default report generates 30 products"""
        product_list = generate_products()
        self.assertEqual(len(product_list), 30)

    def test_legal_names(self):
        product_list = generate_products()
        for product in product_list:
            words = product.name.split(sep=' ')
            self.assertEqual(len(words), 2)
            self.assertIn(words[0], ADJECTIVES)
            self.assertIn(words[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
