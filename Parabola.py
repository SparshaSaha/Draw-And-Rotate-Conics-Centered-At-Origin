from Conic import Conic
import math
import numpy as np

class Parabola(Conic):
    def __init__(self, a, angle):
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

a = int(input())
angle = float(input())

parabola = Parabola(a, angle)
parabola.drawParabola()
