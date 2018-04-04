import turtle

def drawShapes():
    """
    Draws a single square
    """
    #create two turtles and open a window to draw in
    brad = turtle.Turtle()
    angie = turtle.Turtle()
    window = turtle.Screen()

    #color window background gray
    window.bgcolor("gray")

    #color angie and her lines blue, and make her a square
    angie.color("blue")
    angie.pencolor("blue")
    angie.shape("square")

    #color brad, his lines, and the filling of his square white, and make
    #him a circle
    brad.color("white")
    brad.pencolor("white")
    brad.fillcolor("white")
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

    #have angie make a circle of diameter 100px
    angie.circle(100)

    #tell our window to close when clicked on
    window.exitonclick()

drawShapes()
