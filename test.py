import unittest

from materials import RoughOpening


class TestRoughOpening(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        self.r_opening4sides = RoughOpening(top_width=48.5, bottom_width=48.5, left_height=60.5, right_height=60.5)
        self.r_opening3sides = RoughOpening(top_width=36, left_height=82.5, right_height=82.5)
        
    def test_4sided_get_total_inches(self):
        """
        Test that it can sum a list of integer properties
        """
        result = self.r_opening4sides.getTotalInches()
        self.assertEqual(result, 218)
        
    def test_3sided_get_total_inches(self):
        """
        Test that it can sum a list of integer properties
        """
        result = self.r_opening3sides.getTotalInches()
        self.assertEqual(result, 201)        

if __name__ == '__main__':
    unittest.main()