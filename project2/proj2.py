'''
Luke Rader
This scene depicts awesome daytime setting with a house, a tree, and some clouds,

'''

# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math


def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10):
    """Draw a curved line"""
    segment_length = length / segments
    original_heading = t.heading()
    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)
    t.setheading(original_heading)


def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


# YOU MUST add function calls in this draw_scene function


# This function constructs the entire scene by calling predefined 
# shape creating functions. Each object in the scene is built from
# basic geometric shapes and positioned using jump_to() to prevent
# unwanted lines between elements.
def draw_scene(t):
    """Draw a colorful scene using provided turtle functions"""

    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    
    # Ground
   
    # The ground is represented by a large rectangle placed at the bottom
    # of the screen to simulate grass.

    jump_to(t, -400, -100)
    draw_rectangle(t, 800, 300, "green")


    # Sun
    
    jump_to(t, 250, 180)
    draw_circle(t, 50, "yellow")

     # SUn is created by using a circle positioned in the sky, filled with a "sunny" color!
   
   
    # House base
    
    jump_to(t, -110, 100)
    draw_square(t, 200, "beige")

   
    # House roof
    
    jump_to(t, -130, 100)
    draw_triangle(t, 240, "red")
    
    #The house is created using a square for the base and a triangle
    # for the roof.
   
   
    # Tree trunk
   
    jump_to(t, 180, -20)
    draw_rectangle(t, 30, 80, "brown")
 
    # Tree leaves
  
    jump_to(t, 190, -25)
    draw_circle(t, 50, "green")
    # The tree is composed of a rectangle for the trunk and a circle
    # for the leaves to create a simple but recognizable object

   
   
   
   
    # Clouds
   
    jump_to(t, -250, 200)
    draw_circle(t, 25, "white")
    jump_to(t, -220, 210)
    draw_circle(t, 30, "white")
    jump_to(t, -190, 200)
    draw_circle(t, 25, "white")
    # Clouds are formed by overlapping circles to give a more realistic appearanc 
    


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# i am very confused what this final text does. AI didnt explain it very well. And the description is confusing. SORRY! 
if __name__ == "__main__":
    main()
