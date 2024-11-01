import turtle

def drawRectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(4):
        t.forward(w)
        t.left(90)

def drawSquare(tx, sz):        # a new version of drawSquare
    drawRectangle(tx, sz, sz)

wn = turtle.Screen()             # Set up the window
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess

drawSquare(tess, 50)

wn.exitonclick()
