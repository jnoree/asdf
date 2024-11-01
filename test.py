import turtle

def drawRectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def drawRectangleWithSize(tx, width, height):
    """Draw a rectangle using the turtle with specified width and height."""
    drawRectangle(tx, width, height)

wn = turtle.Screen()  # Set up the window
wn.bgcolor("lightgreen")

# Get the underlying Tkinter window
turtle_window = wn.getcanvas().winfo_toplevel()

# Set the window position to the left side of the screen
x_position = 0  # Change this for different positions
y_position = 100  # Set desired y position
turtle_window.geometry("+{}+{}".format(x_position, y_position))

tess = turtle.Turtle()  # create tess

# Draw a rectangle with specified width and height
drawRectangleWithSize(tess, 100, 50)  # Change these values as needed

wn.exitonclick()
