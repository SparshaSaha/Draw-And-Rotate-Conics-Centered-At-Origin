from Conic import Conic
import math
import numpy as np

# We are creating Ellipse class which inherits Conic class
class Ellipse(Conic):

    def __init__(self, a, b, angle):
        super().__init__(3*a, 3*b, angle)
        self.a = a
        self.b = b

    def equate(self, x):
        root = (self.b**2*(1-((x)**2/self.a**2)))
        if root >= 0:
            return math.sqrt(root)
        return None

    def drawEllipse(self):
        self.plotCanvas()

    def createXCoords(self):
        # Create a linspace of XCoords
        xCoords = np.arange(-1*self.a, self.a, 0.0005).tolist()
        return xCoords

print("Enter 'a' 'b' and 'angle' one by one")
a = int(input())
b = int(input())
angle = float(input())

ellipse = Ellipse(a, b, angle)
ellipse.drawEllipse()
