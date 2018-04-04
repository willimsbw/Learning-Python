import turtle

def drawShapes():
    """
    Draws a square, a circle, and then a triangle.
    """
    #create three turtles and open a window to draw in
    squareTurtle = turtle.Turtle()
    circleTurtle = turtle.Turtle()
    triangleTurtle = turtle.Turtle()
    window = turtle.Screen()

    #color window background gray
    window.bgcolor("gray")

    #color triangleTurtle and its lines orange, and make it a triangle
    triangleTurtle.color("orange")
    triangleTurtle.pencolor("orange")
    triangleTurtle.shape("triangle")

    #color circleTurtle and its lines blue, and make it a circle
    circleTurtle.color("blue")
    circleTurtle.pencolor("blue")
    circleTurtle.shape("circle")

    #color squareTurtle, its lines, and the filling of its square white, and make
    #it a square
    squareTurtle.color("white")
    squareTurtle.pencolor("white")
    squareTurtle.fillcolor("white")
    squareTurtle.shape("square")

    #tell python to fill following shapes drawn by squareTurtle
    squareTurtle.begin_fill()

    #have squareTurtle draw a square
    for i in range(4):
        #move forward 100 pixels
        squareTurtle.forward(100)
        #turn right 90 degrees
        squareTurtle.right(90)

    #Tells it that the shape is made so apply the filling
    squareTurtle.end_fill()

    #have circleTurtle make a circle of diameter 100px
    circleTurtle.circle(100)

    #orient triangleTurtle away from other shapes
    triangleTurtle.left(180)
    #have triangleTurtle draw a triangle
    for i in range(3):
        #move forward 100 pixels
        triangleTurtle.forward(150)
        #turn left 120 degrees
        triangleTurtle.left(120)

    #tell our window to close when clicked on
    window.exitonclick()

drawShapes()
