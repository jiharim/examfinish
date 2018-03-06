# -*- coding: utf-8 -*-

import unittest
import Yearin



class YearinTestCase(unittest.TestCase):
    def test_year(self):
        self.assertEqual(Yearin.yearin(2100),'평년')
        self.assertEqual(Yearin.yearin(1988),'윤년')
        self.assertEqual(Yearin.yearin(1600),'윤년')

    
if __name__=="__main__":
    unittest.main(verbosity=2)
