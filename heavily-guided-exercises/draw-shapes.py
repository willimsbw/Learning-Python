import turtle

def drawSun():
    """
    Draws a square, a circle, and then a triangle.
    """

    def drawSquare(squareTurtle):
        """
        Draws a white, filled square 100 pixels long with a white square cursor
        """
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

    def drawCircle(circleTurtle):
        """
        Draws a blue unfilled circle with a blue circle cursor with radius 50px
        """
        #color circleTurtle and its lines blue, and make it a circle
        circleTurtle.color("blue")
        circleTurtle.pencolor("blue")
        circleTurtle.shape("circle")
        #have circleTurtle make a circle of radius 50 pixels
        circleTurtle.circle(50)

    def drawTriangle(triangleTurtle):
        """
        Draws an orange unfilled equilateral triangle with an orange triangle
        cursor and sides 150px
        """
        #color triangleTurtle and its lines orange, and make it a triangle
        triangleTurtle.color("orange")
        triangleTurtle.pencolor("orange")
        triangleTurtle.shape("triangle")
        #orient triangleTurtle away from other shapes
        triangleTurtle.left(180)
        #have triangleTurtle draw a triangle
        for i in range(3):
            #move forward 100 pixels
            triangleTurtle.forward(150)
            #turn left 120 degrees
            triangleTurtle.left(120)

    window = turtle.Screen()
    window.bgcolor("gray") #color window background gray
    brad = turtle.Turtle()

    #draw 36 filled squares to make a sun
    for i in range(36):
        drawSquare(brad)
        #turn right 10 degrees
        brad.right(10)

    #tell our window to close when clicked on
    window.exitonclick()

drawSun()
