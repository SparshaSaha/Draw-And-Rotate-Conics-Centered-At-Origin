# Conic is a generic class which can be used to plot finite conics
# Till now we cannot plot HyperBola as it is an infinite figure but it is going to be a WIP.

class Conic(object):

    def __init__(self,a ,b):
        self.a = a
        self.b = b
        self.canvas = None

    # Method that creates the Canvas
    # The Canvas will be of variable length depending on a and b
    # Thus we create a canvas 
    def createCanvas(self):
        self.canvas = [[255 for i in range(0, 3*self.b+1)]for j in range(0, 3*self.a+1)]
