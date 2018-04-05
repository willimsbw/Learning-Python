import turtle
import time

def drawKochSide(length, n, someTurtle):
    """
    Draws a single side of a Koch snowflake fractal with the given turtle

    length: int. The distance between each end of the snowflake side
    n: int. The orders of magnitude for the fractal. How many levels of the
    pattern you want it to draw.
    someTurtle: a turtle object
    """
    #if we still have orders of magnitude left to draw
    if n > 0:
        #unless n = 1, draws n-1 basic fractal shapes 4 times, turning i degrees
        #between each. if n = 1, draws 1 basic fractal shape.
        for i in [60, -120, 60, 0]:
            #call the function again, reducing line length to 1/3rd, the order of
            #magnitude by 1, and keeping the same turtle
            drawKochSide(length/3, n-1, someTurtle)
            #rotate i degrees before calling the next recursion
            someTurtle.left(i)
    else:
        #if there aren't further iterations, draw a straight line. Each recursive
        #call reduces the length of this line.
        someTurtle.forward(length)

def drawKochWhole(sideLength, n, someTurtle, numSides, reverse=False):
    """
    Draws a whole, filled koch snowflake fractal with a given Turtle

    sideLength: int. The distance between ends for each side of the snowflake
    n: int. How many orders of magnitude (e.g., levels of the pattern) you want
    it to draw
    someTurtle: a turtle object.
    numSides: int. The number of sides you want the snowflake to have
    reverse: bool, default = False. If true, draws the sides facing inward
    rather than outward.
    """
    #figure out what angle the turtle needs to turn based on the number of sides
    angle = 360/numSides

    #fill the final shape with black
    someTurtle.fillcolor("black")
    someTurtle.begin_fill()

    for i in range(numSides):
        drawKochSide(sideLength, n, someTurtle)
        if reverse:
            someTurtle.left(angle)
        else:
            someTurtle.right(angle)

    someTurtle.end_fill()

brad = turtle.Turtle()
window = turtle.Screen()

drawKochSide(200, 3, brad)
time.sleep(5)
window.resetscreen()
drawKochWhole(300, 2, brad, 4)

window.exitonclick()
