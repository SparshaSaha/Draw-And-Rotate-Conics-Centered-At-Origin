# Conic is a generic class which can be used to plot finite conics
# Till now we cannot plot HyperBola as it is an infinite figure but it is going to be a WIP.
import math
import numpy as np
import matplotlib.pyplot as plt

class Conic(object):

    def __init__(self, row, col, angle):
        self.row = row
        self.col = col
        self.canvas = None
        self.white = 255
        self.black = 0
        self.angle = angle
        
    
    # Method that creates the Canvas
    # The Canvas will be of variable length depending on a and b
    # Thus we create a dynamic canvas which changes depending on a and b values to account for the rotation of the conic
    def createCanvas(self):
        self.canvas = [[self.white for i in range(0, self.col + 1)]for j in range(0, self.row + 1)]

    # We assume that origin is at (0,0) as this makes it easier to rotate the conic
    # But our canvas is a 2D array(which is later converted to a numpy array and then converted to an image)
    # Thus according to array Indexing we have our origin at (-a,b) which is nothing but (0,0) in Array indexing method
    # So an origin shifting is necessary at the time of plotting. This is exactly what has been done in this method
    def findShiftedCoordinatesWithAxisAsArrayIndexing(self, x, y):
        shiftedXCoord = x + self.row/2
        shiftedYCoord = y + self.col/2
        return (shiftedXCoord, shiftedYCoord, self.withinCanvasBoundaries(shiftedXCoord, shiftedYCoord))

    def withinCanvasBoundaries(self, x, y):
        if x < self.row and y < self.col and x >= 0 and y >= 0:
            return True
        return False
    
    # Out plotting would ideally be one pixel thick right now
    # But that makes things look bad
    # Thus we are filling the nearby pixels with this method to make the conic look better
    # Alternatively we can use opening as well to close the gap but that would be of more complexity
    # This algorithm here is BigO(constant) complexity
    def plotNearbyRegions(self, x, y):
        if self.withinCanvasBoundaries(x-1, y):
            self.canvas[x-1][y] = self.black
            
        if self.withinCanvasBoundaries(x-1, y-1):
            self.canvas[x-1][y-1] = self.black
            
        if self.withinCanvasBoundaries(x, y-1):
            self.canvas[x][y-1] = self.black

        if self.withinCanvasBoundaries(x+1, y):
            self.canvas[x+1][y] = self.black

        if self.withinCanvasBoundaries(x+1, y+1):
            self.canvas[x+1][y+1] = self.black

        if self.withinCanvasBoundaries(x, y+1):
            self.canvas[x][y+1] = self.black

        if self.withinCanvasBoundaries(x-1, y+1):
            self.canvas[x-1][y+1] = self.black

        if self.withinCanvasBoundaries(x+1, y):
            self.canvas[x+1][y-1] = self.black

    # Plotting the X and Y Axes 
    def plotAxes(self):
        for i in range(0, self.row):
            self.canvas[i][int(self.col/2)] = self.black

        for j in range(0, self.col):
            self.canvas[int(self.row/2)][j] = self.black
        
    def plotCanvas(self):
        self.createCanvas()
        self.plotAxes()
        XCoords = self.createXCoords()

        for coord in XCoords:
            yCoordVal = self.equate(coord)
            if yCoordVal == None:
                continue

            # Rotating particular point by given angle
            roX1 = coord*math.sin(math.radians(self.angle)) - yCoordVal*math.cos(math.radians(self.angle))
            roY1 = coord*math.cos(math.radians(self.angle)) + yCoordVal*math.sin(math.radians(self.angle))

            # Rotated reflected coordinates across X axis
            roX2 = coord*math.sin(math.radians(self.angle)) - (-1) * yCoordVal*math.cos(math.radians(self.angle))
            roY2 = coord*math.cos(math.radians(self.angle)) + (-1) * yCoordVal*math.sin(math.radians(self.angle))

            shiftedCoord1 = self.findShiftedCoordinatesWithAxisAsArrayIndexing(roX1, roY1)
            shiftedCoord2 = self.findShiftedCoordinatesWithAxisAsArrayIndexing(roX2, roY2)

            # Plotting on canvas if rotated points are within Canvas boundaries
            if shiftedCoord1[2]:
                self.canvas[int(shiftedCoord1[0])][int(shiftedCoord1[1])] = self.black
                self.plotNearbyRegions(int(shiftedCoord1[0]), int(shiftedCoord1[1]))
            if shiftedCoord2[2]:
                self.canvas[int(shiftedCoord2[0])][int(shiftedCoord2[1])] = self.black
                self.plotNearbyRegions(int(shiftedCoord2[0]), int(shiftedCoord2[1]))

        # Converting to numpy array and showing it as Image
        plt.imshow(np.array(self.canvas), cmap="gray")
        plt.show()
