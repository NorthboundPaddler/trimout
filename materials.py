class RoughOpening(object):
    def __init__(self, top_width=None, bottom_width=None, left_height=None, right_height=None):
        self.top = top_width
        self.bottom = bottom_width
        self.left = left_height
        self.right = right_height
        self.sides = self.setSides()
    
    def setSides(self):
        sides = []
        for side in (self.top, self.bottom, self.left, self.right):
            if side:
                sides.append(side)
        return sides
    
    def getTotalInches(self):
        total = 0
        for side in self.sides:
            total += side
        return total
    
    def __str__(self):
        return f"<Rough Opening {self.top}x{self.left}>"
    
class Window(RoughOpening):
    def __init__(self, top_width=None, bottom_width=None, left_height=None, right_height=None, jamb_thickness = 0.75, jamb_setback = 0.75):
        self.jamb_thickness = jamb_thickness
        self.jamb_setback = jamb_setback
        RoughOpening.__init__(self, top_width, bottom_width, left_height, right_height)
   
    def getAllTrimLengthsFromInsideJambEdge(self, trim_thickness=3, corner_style="90_TOPS_EXTENT"):
        if   corner_style == '90_TOPS_EXTENT':
            top_btm_height = self.top - (2*self.jamb_setback) - (2*self.jamb_thickness) + (2*trim_thickness)
            side_height = self.left - (2*self.jamb_setback) - (2*self.jamb_thickness)
        
        return (top_btm_height, side_height)
    
    def getTotalTrimInches(self,  trim_thickness=3, corner_style="90_TOPS_EXTENT"):
        top_btm_inches, sides_inches  = self.getAllTrimLengthsFromInsideJambEdge()
        return (top_btm_inches*2) + (sides_inches*2)

class Board(object):
    def __init__(self, width=3, length=90):
        self.width = width
        self.length = length
        self.original_length = self.length
        self.pieces = [self.length]
        
    def cut(self, cutLength):
        if cutLength > self.length:
            return False
        else:    
            self.length = self.length - cutLength
            self.pieces.remove(self.length + cutLength)
            self.pieces.append(self.length)
            self.pieces.append(cutLength)
            self.pieces.sort()
            return cutLength