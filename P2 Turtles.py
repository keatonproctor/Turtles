'''
Project Name: P2 Turtles
Author: Keaton Proctor
Due Date: 06/19/2021
Course: CS1400-zzz

This program will use 4 different functions passing in different parameters to modify geometric
shapes that will be drawn by using the 'Turtle' drawing attributes. Each shape will have parameters
such as height, width, fill color, border color, tilt, etc. The final result will have a triangle,
square, rectangle, a large circle and a few smaller circles, some put together to make a cloud. These shapes
will be drawn in a window that is specifically sized by asking the user window width and height inputs.'''

import turtle  
    
def main():
    steve = turtle.Turtle()
    s = turtle.Screen()
    
    steve.shape("turtle")
    steve.speed(10)
    
    try:
        window_width = input("Please enter the window width: ")
        window_width = int(window_width)
        
        window_height = input("Please enter the window height: ")
        window_height = int(window_height)
        
    except ValueError:
        print("Enter only postive integers for width and height.")
        return
    
    if window_width < 1 or window_height < 1:
       print("Enter only postive integers for width and height.")
       return
    
    s.setup(window_width, window_height, 0, 0)
    
    
    #Functions
    draw_square(steve, -200, -300, 400, 400, "indian red", "tan")
    draw_triangle(steve, -200, 101, 135, "light gray", "sea green", 25)
    draw_rectangle(steve, -60, -300, 200, 120, "pink", "maroon")
    draw_circle(steve, 100, 100, 67, "yellow", "blue violet")
    
    #Drawing Cloud with draw_circle
    draw_circle(steve, -300, 263, 35, "light sky blue", "light sky blue")
    draw_circle(steve, -270, 265, 40, "light sky blue", "light sky blue")
    draw_circle(steve, -240, 260, 35, "light sky blue", "light sky blue")
    draw_circle(steve, -210, 220, 40, "light sky blue", "light sky blue")
    draw_circle(steve, -250, 200, 35, "light sky blue", "light sky blue")
    draw_circle(steve, -290, 200, 40, "light sky blue", "light sky blue")
    draw_circle(steve, -320, 220, 35, "light sky blue", "light sky blue")
    

# (3) Add functions here that your main program calls to do stuff.
def draw_square(steve, x, y, width, height, pen, fill):
    '''
    - draw_square will draw the a square (house) shape with the turtle
    - Steve is the turtle
    - X is the X coordinate
    - Y is the Y coordinate
    - Height is the height of the square
    - Pen is the border color ("string")
    - Fill is the inside color ("string")
    '''
    steve.up()
    steve.goto(-200, -300)
    steve.setheading(0)
    steve.pencolor(pen)
    steve.fillcolor(fill)
    steve.down()
    
    #Drawing the Square
    steve.begin_fill()
    for i in range(2):
        steve.forward(width)
        steve.left(90)
        steve.forward(height)
        steve.left(90)
    steve.end_fill()
    
#End of draw_square()
    
def draw_triangle(steve, x, y, angle, pen, fill, rotation):
    '''
    - draw_triangle will draw a triangle (roof) above the draw_square with the turtle
    - Steve is the turtle
    - X is the X coordinate
    - Y is the Y coordinate
    - Angle is the angle of each side of the triangle
    - Fill is the inside color ("string")
    - Rotation will tilt the triangle up or down
    '''
    steve.up()
    steve.goto(x,y)
    steve.setheading(rotation)
    steve.pencolor(pen)
    steve.fillcolor(fill)
    steve.down()
    
    #Drawing the Triangle
    steve.begin_fill()
    steve.forward(400)
    for i in range(1):
        steve.left(angle)
        steve.forward(283)
        steve.left(90)
    steve.end_fill()
    
#End of draw_triangle()
    
def draw_rectangle(steve, x, y, height, width, pen, fill):
    '''
    - draw_rectangle will draw a rectangle (door) inside the draw_square with the turtle
    - Steve is the turtle
    - X is the X coordinate
    - X is the Y coordinate
    - Height is the height of the rectangle
    - Width is the length of the rectangle
    - Pen is the border color ("string")
    - Fill is the inside color ("string")
    '''
    steve.up()
    steve.goto(-60,-300)
    steve.setheading(0)
    steve.pencolor(pen)
    steve.fillcolor(fill)
    steve.down()
    
    #Drawing the Rectangle
    steve.begin_fill()
    for i in range(2):  
        steve.forward(width)
        steve.left(90)
        steve.forward(height)
        steve.left(90)
    steve.end_fill()
    
#End of draw_rectangle()
    
def draw_circle(steve, x, y, radius, pen, fill):
    '''
    - draw_circle will draw a circle (rock) on top the draw_square with the turtle
    - Steve is the turtle
    - X is the X coordinate
    - Y is the Y coordinate
    - Pen is the border color ("string")
    - Fill is the inside color ("string")
    '''
    steve.up()
    steve.goto(x, y)
    steve.setheading(0)
    steve.pencolor(pen)
    steve.fillcolor(fill)
    steve.down()
    
    #Drawing the Circle
    steve.begin_fill()
    steve.circle(radius)
    steve.end_fill()
    
#End of draw_circle()

#End of Program
if __name__ == "__main__":
    main()