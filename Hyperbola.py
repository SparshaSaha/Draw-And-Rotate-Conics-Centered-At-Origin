from Conic import Conic
import math
import numpy as np

class Hyperbola(Conic):

    def __init__(self, a, b, angle):
        super().__init__(3*a, 3*b, angle)
        self.a = a
        self.b = b

    def equate(self, x):
        root = (self.b**2*((x**2/self.a**2) - 1))
        if root >= 0:
            return math.sqrt(root)
        return None

    def drawHyperbola(self):
        self.plotCanvas()

    def createXCoords(self):
        # Create a linspace of XCoords
        xCoords1 = np.arange(-5*self.a, -1*self.a, 0.005).tolist()
        xCoords2 = np.arange(self.a, 5*self.a, 0.005).tolist()
        xCoords = xCoords1 + xCoords2
        return xCoords

print("Enter 'a' 'b' and 'angle' one by one")
a = int(input())
b = int(input())
angle = float(input())

hyperbola = Hyperbola(a, b, angle)
hyperbola.drawHyperbola()
