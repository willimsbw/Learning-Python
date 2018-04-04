import turtle

def drawSquare():
    """
    Draws a single square
    """
    #create a turtle named brad
    brad = turtle.Turtle()
    #open a window for brad to draw on
    window = turtle.Screen()
    #color window background red
    window.bgcolor("red")
    #color the turtle white
    brad.color("white")
    #color the lines white
    brad.pencolor("white")
    #color the filling of the square white
    brad.fillcolor("white")
    #Make brad a circle
    brad.shape("circle")

    #tell it to fill the square that's created with our pre-determined color
    brad.begin_fill()

    #move forward, then turn right. Repeat 4 times
    for i in range(4):
        #move forward 100 pixels
        brad.forward(100)
        #turn right 90 degrees
        brad.right(90)

    #Tells it that the shape is made so apply the filling
    brad.end_fill()

    #tell our window to close when clicked on
    window.exitonclick()

drawSquare()
