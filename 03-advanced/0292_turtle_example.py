import turtle  # this imports a library called "turtle". A library is (typically someone else's) python code, that you can use in your own program.

def demo():  # demonstration of basic turtle commands
    tom.speed(10)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.circle(50)  # draw a circle with radius 50
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.goto(-100, -200)  # move to coordinates -100, -200  (0, 0 is the middle of the screen)
    tom.home()  # return to the original position in the middle of the window

def circle(radius):
    tom.pendown()
    tom.circle(radius)


def move_to(x, y):
    tom.penup()
    tom.goto(x, y)

def square(size):
    tom.pendown()
    for x in range(4):
        tom.forward(size)
        tom.right(90)

def triangle(length):
    tom.pencolor("green")
    for x in range(3):
        tom.forward(length)
        tom.right(120)

def triangle_color(length, color):
    tom.pencolor(color)
    for x in range(3):
        tom.forward(length)
        tom.right(120)

def many_squares(number_of_squares, size, distance):
    tom.penup()
    tom.goto(150, 150)
    tom.pendown()
    tom.pencolor("red")
    for x in range(number_of_squares):
        square(size)
        tom.forward(distance)

def many_circles():
    tom.pencolor("blue")
    for x in range(10):
        move_to(-100, 100)
        circle(50)
        tom.right(40)
    tom.left(40)

def draw_square_at(length, x, y):
    tom.goto(x, y)
    for x in range(4):
        tom.forward(length)
        tom.right(90)

def draw_grid(columns, rows, size):
    for x in range(rows):
        for x in range(columns):
            square(size)
            tom.forward(size)
        tom.backward(size * columns)
        tom.right(90)
        tom.forward(size)
        tom.left(90)


tom = turtle.Turtle()  # create an object named tom of type Turtle
demo()
circle(100)
move_to(-150, -150)
square(100)
triangle(150)
triangle_color(200, "blue")
many_squares(6, 10, 20)
many_circles()
draw_square_at(100, -200, 0)
draw_grid(5, 5, 20)
turtle.done()  # keep the turtle window open after the program is done
