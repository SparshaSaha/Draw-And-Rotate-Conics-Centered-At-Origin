# Conic is a generic class which can be used to plot finite conics
# Till now we cannot plot HyperBola as it is an infinite figure but it is going to be a WIP.
import math
import numpy as np
import matplotlib.pyplot as plt

class Conic(object):

    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.canvas = None
        self.white = 255
        self.black = 0
        self.angle = angle
        
    
    # Method that creates the Canvas
    # The Canvas will be of variable length depending on a and b
    # Thus we create a dynamic canvas which changes depending on a and b values to account for the rotation of the conic
    def createCanvas(self):
        self.canvas = [[self.white for i in range(0, 3*self.b+1)]for j in range(0, 3*self.a+1)]

    # We assume that origin is at (0,0) as this makes it easier to rotate the conic
    # But our canvas is a 2D array(which is later converted to a numpy array and then converted to an image)
    # Thus according to array Indexing we have our origin at (-a,b) which is nothing but (0,0) in Array indexing method
    # So an origin shifting is necessary at the time of plotting. This is exactly what has been done in this method
    def findShiftedCoordinatesWithAxisAsArrayIndexing(self, x, y):
        shiftedXCoord = x + 1.5 * self.a
        shiftedYCoord = y + 1.5 * self.b
        return (shiftedXCoord, shiftedYCoord)

    def plotCanvas(self):
        self.createCanvas()
        # Create a linspace of XCoords
        XCoords = np.arange(-1*self.a, self.a, 0.0005).tolist()

        for coord in XCoords:
            yCoordVal = self.equate(coord)

            # Rotating particular point by given angle
            roX1 = coord*math.sin(math.radians(self.angle)) - yCoordVal*math.cos(math.radians(self.angle))
            roY1 = coord*math.cos(math.radians(self.angle)) + yCoordVal*math.sin(math.radians(self.angle))

            # Rotated reflected coordinates across X axis
            roX2 = coord*math.sin(math.radians(self.angle)) - (-1) * yCoordVal*math.cos(math.radians(self.angle))
            roY2 = coord*math.cos(math.radians(self.angle)) + (-1) * yCoordVal*math.sin(math.radians(self.angle))

            shiftedCoord1 = self.findShiftedCoordinatesWithAxisAsArrayIndexing(roX1, roY1)
            shiftedCoord2 = self.findShiftedCoordinatesWithAxisAsArrayIndexing(roX2, roY2)

            # Plotting on canvas
            self.canvas[int(shiftedCoord1[0])][int(shiftedCoord1[1])] = self.black
            self.canvas[int(shiftedCoord2[0])][int(shiftedCoord2[1])] = self.black

        # Converting to numpy array and showing it as Image
        plt.imshow(np.array(self.canvas), cmap="gray")
        plt.show()
