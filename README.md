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

