class Button:
    """Button. Invisible object on screen, defined as set of points."""

    def __init__(self, points, text, mode):
        self.from_point, self.to_point = points
        self.text = text
        self.mode = mode

    def hover(self, mouse):
        """Check if the mouse is over button"""
        return (self.from_point[0] < mouse[0] < self.to_point[0]
                and self.from_point[1] < mouse[1] < self.to_point[1])
