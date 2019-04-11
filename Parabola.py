from Conic import Conic
import math
import numpy as np

class Parabola(Conic):
    def __init__(self, a, angle):
        a = self.bringToScale(a)
        super().__init__(12*a, 12*a, angle)
        self.a = a

    def equate(self, x):
        root = 4*self.a*x
        if root >= 0:
            return math.sqrt(root)
        return None

    def createXCoords(self):
        # Create a linspace of XCoords
        xCoords = np.arange(0, 24*self.a, 0.005).tolist()
        return xCoords

    def drawParabola(self):
        self.plotCanvas()

    def bringToScale(self, a):
        if a < 10:
            self.scale = 10
            return a*10
        else:
            while a > 100:
                a = int(a/10)
            return a

print("Enter 'a' and 'angle' one by one")
a = int(input())
angle = float(input())

parabola = Parabola(a, angle)
parabola.drawParabola()
