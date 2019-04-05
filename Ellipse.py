from Conic import Conic
import math

# We are creating Ellipse class which inherits Conic class
class Ellipse(Conic):

    def __init__(self, a, b, angle):
        super().__init__(a, b, angle)

    def equate(self, x):
        root = (self.b**2*(1-((x)**2/self.a**2)))
        y = math.sqrt(root)
        return y

    def drawEllipse(self):
        self.plotCanvas()

print("Enter 'a' 'b' and 'angle' one by one")
a = int(input())
b = int(input())
angle = float(input())

ellipse = Ellipse(a, b, angle)
ellipse.drawEllipse()
