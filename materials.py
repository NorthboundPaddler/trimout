class RoughOpening(object):
    def __init__(self, top_width=None, bottom_width=None, left_height=None, right_height=None):
        self.top = top_width
        self.bottom = bottom_width
        self.left = left_height
        self.right = right_height
        self.sides = setSides()
    
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
    