# Conics

## Introduction
Recently I came across a very interesting problem. One of my friends(read **Crush** :stuck_out_tongue:) was given an assignment in her graphics class which required them to plot an ellipse without using any mathematical plotting libraries.
The problem seems easy at first but probably it is not. Since you cannot use any library, it is not an easy job to plot **Mr. Ellipse**.
And to make problems worse, turns out they needed to **rotate the Ellipse as well, given some angle of rotation**.

But it's my Crush nevertheless and no guy in the world would leave a chance to impress his crush I guess. Would you? I guess not. :stuck_out_tongue:
So we decided to work on some solution together. Well we came up with more than one(She is a pretty smart one. Nice catch eh? :wink:) and then we chose the best one(according to her) among them.

Just to put things in perspective, the main requirement was to plot an ellipse without using any kind of plotting libraries and 
rotate the ellipse as well given any angle.

**Constraints : The Ellipse will be centered at origin**

## Requirements and Installation
### Libraries
* OpenCv-Python
* Numpy

### Installation
* Install pip3 by downloading [this](https://bootstrap.pypa.io/get-pip.py) file and running it on your machine using python3

After installing pip3, install the following using these commands:
* `pip3 install opencv-python`
* `pip3 install numpy`

### Cloning the repository
Use the following command to clone the repository into your local system:

`git clone https://github.com/SparshaSaha/Draw-And-Rotate-Conics-Centered-At-Origin.git`

# Architecture and Strategy
## Plotting Strategy
The idea is to plot a Conic and be able to rotate it without using any library. Now we need to understand how we can exactly plot a figure. We know that any image can be represented as a numpy array. This concept is the base for our plot. We create a **2D numpy array** of **variable length**(reason will be discussed later) and plot the points there. By plotting we mean we fill a plot pixel with **0(stands for black in colour coding)**.

The basic idea is to create a linspace of **X** values and calculate the corresponding **Y** values and plot the **Y** values on the canvas(nothing but the numpy array).

Ideally this is what our canvas really is:

![picture alt](https://github.com/SparshaSaha/Draw-And-Rotate-Conics-Centered-At-Origin/blob/master/Images/CanvasEmpty.png)
The rectangle represents our canvas and each smaller square inside the rectangle represents **one pixel**.
Now we need to somehow fill the required pixels with black in order to give shape to our Conic.

Now very roughly this is how a circle will look like(It looks really bad. But just for reference)

![picture alt](https://github.com/SparshaSaha/Draw-And-Rotate-Conics-Centered-At-Origin/blob/master/Images/CanvasCircle.png)
## Origin shifting
Ideally our conic(as seen in case of the circle), will have the centre as the centre of the canvas. Well that will be our **mathematical centre(0,0)** but since our canvas is a numpy array, our actual centre(0,0) will be nothing but (-a,b)

where **a** is length of canvas and **b** is the breadth of the canvas.

Lets look at this picture to have a better understanding.
![picture alt](https://github.com/SparshaSaha/Draw-And-Rotate-Conics-Centered-At-Origin/blob/master/Images/CanvasIndexing.png)

Thus it is evident we need to shift the orign at the time of plotting the figure.

## Creating X coordinates
We will create **X** coordinates in a range for which **Y** coordinates will be Real(Not Imaginary :stuck_out_tongue:)

**For Example** :- 
* In case of Ellipse with axes as **a** and **b** we need to create **X** coordinates in range **(-a,a)**.
* In case of parabola with focus at **(a,0)** we need to generate **X** coordinates in range **(0, Infinity or Edge of canvas)**

Next we need to calculate the **Y** values for those **X** coordinates and origin shift them to Array-Indexing based origin and then plot them as canvas[originShiftedX][originShiftedY] = **Black Colour**

## Rotation Of Figure
Now coming to the most interesting part that is rotation. Now we chose to use Mathematical (0,0) as origin because it is easier to rotate a figure centered at origin.

**It's east to understand that for a figure centered at origin, If we can rotate all the Y coordinates by the required angle, the figure gets rotated as well**.

This is the approach that we have used.

For rotating each **X** and **Y** coordinates, we have used the following.

`X' = X*cos(angle) - Y*sin(angle)`

`Y' = X*sin(angle) + Y*cos(angle)`

Thus rotating each pair of coordinates and plotting them on the canvas gives us the rotated figure.

## About the Repository
The repo contains a Base Class **Conic** which contains all the necessary functions like Plotting, Canvas creation etc. common to all conics. The comes inherited classes like Ellipse, Parabola and Hyperbola which contain funtionalities different to each figure.

To test the repo, simply run either **Ellipse.py, Parabola.py, Hyperbola.py** and follow the steps. In no time you can see your plotted Conic.

Thanks for reading.

**DEMO TIME**

Rotated Ellipse:
![picture alt](https://github.com/SparshaSaha/Draw-And-Rotate-Conics-Centered-At-Origin/blob/master/Images/RotatedEllipse.png)

Rotated Parabola:
![picture alt](https://github.com/SparshaSaha/Draw-And-Rotate-Conics-Centered-At-Origin/blob/master/Images/RotatedParabola.png)

Rotated Hyperbola:
![picture alt](https://github.com/SparshaSaha/Draw-And-Rotate-Conics-Centered-At-Origin/blob/master/Images/RotatedHyperbola.png)

Oh! The Crush that I was talking about, we are going on a date Next Week! Coding can do Wonders! TING! :wink:
