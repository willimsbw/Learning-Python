import turtle

def drawSquare():
    """
    Draws a single square
    """
    #create a turtle named brad
    brad = turtle.Turtle()
    #create a window for brad to draw on
    window = turtle.Screen()
    #color window background red
    window.bgcolor("red")
    #move forward, then turn right. Repeat 4 times
    for i in range(4):
        #move forward 100 steps
        brad.forward(100)
        #turn right 90 degrees
        brad.right(90)

    #tell our window to close when clicked on
    window.exitonclick()

drawSquare()
