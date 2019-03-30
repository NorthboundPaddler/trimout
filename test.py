import unittest

from materials import RoughOpening, Window, Board


class TestRoughOpening(unittest.TestCase):
       
    def setUp(self):
        self.rough_opening_4sides =  RoughOpening(top_width=48.5, bottom_width=48.5, left_height=60.5, right_height=60.5)
        self.rough_opening_3sides =  RoughOpening(top_width=36, left_height=82.5, right_height=82.5)   
        
    def test_4sided_get_total_inches(self):
        """
        Test that it can sum a list of integer properties
        """
        result = self.rough_opening_4sides.getTotalInches()
        self.assertEqual(result, 218)
        
    def test_3sided_get_total_inches(self):
        """
        Test that it can sum a list of integer properties
        """
        result = self.rough_opening_3sides.getTotalInches()
        self.assertEqual(result, 201)        

class TestWindow(unittest.TestCase):
    def setUp(self):
        self.window = Window(top_width=48.5, bottom_width=48.5, left_height=60.5, right_height=60.5)
    
    def test_getAllTrimLengthsFromInsideJambEdge(self):
        '''
        Test that the correct distance of trim is calculated from inside edge of the jamb 
        '''
        result = self.window.getAllTrimLengthsFromInsideJambEdge()
        self.assertEqual(result, (51.5,57.5))
    
    def test_getTotalTrimInches(self):
        '''
        Test that the correct inches of trim is calculated
        '''
        result = self.window.getTotalTrimInches()
        self.assertEqual(result, 218)

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(width=3, length=48)
    
    def test_cutBoard(self):
        result = self.board.cut(cutLength=12)
        self.assertEqual(result, 12)

    def test_cutPieces(self):
        self.board.cut(cutLength=12)
        result = self.board.pieces
        self.assertEqual(result, [12,36])
    
    def test_cutPiecesFailure(self):
        result = self.board.cut(cutLength=60)
        self.assertEqual(result, False)
        
if __name__ == '__main__':
    unittest.main()