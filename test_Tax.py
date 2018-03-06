# -*- coding: utf-8 -*-

import unittest

import Tax


class TaxTestCase(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(Tax.tax(30,10000,True), int(10000*0.1))




if __name__=="__main__":
    unittest.main(verbosity=2)
