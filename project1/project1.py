import turtle

# creating the scene, starting with screen color. 
screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Creating the functions for each item in the scene. 

def draw_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def draw_triangle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_house(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # House base
    draw_square(150, "tan")

    # Roof
    t.left(90)
    t.forward(150)
    t.right(90)
    draw_triangle(150, "brown")

    # Door for houSe!
    t.penup()
    t.goto(x + 60, y)
    t.pendown()
    draw_square(30, "brown")

def draw_tree(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Trunk for tree
    t.fillcolor("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()

    # Leaves for tree
    t.penup()
    t.goto(x + 10, y + 60)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def draw_sun(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

# Creating the flower, used AI to help create the petals. 

def draw_flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Stem
    t.color("green")
    t.setheading(90)
    t.forward(40)

    # Petals
    t.color("red")
    for _ in range(6):
        t.circle(10)
        t.left(60)

# DRAWING SCENE STARTING HERE. Took a while to figure out how to start it, but i figured it out. 

draw_sun(-250, 180)
draw_house(-75, -100)

draw_tree(-250, -100)

draw_flower(-20, -100)
draw_flower(20, -100)
draw_flower(60, -100)

# Finish, had to use AI to remeber how to keep the tab open. 
turtle.done()
