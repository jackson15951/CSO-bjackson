import turtle
import math

def draw_star(length, sides, scale=1.0):
    angle = (1/sides)*360
    outer_angle = 180 - angle
    inner_angle = (180 - outer_angle) / 2
    
    for _ in range(sides):
        turtle.pendown()
        turtle.forward(length * scale)
        turtle.left(outer_angle)
        turtle.forward(length * scale / (2 * math.cos(math.radians(inner_angle))))
        turtle.penup()
        turtle.backward(length * scale / (2 * math.cos(math.radians(inner_angle))))
        turtle.left(inner_angle)
    
    turtle.forward(length * scale * math.cos(math.radians(inner_angle)))
    turtle.left(180 - angle / 2)
    
    for _ in range(sides):
        turtle.pendown()
        turtle.forward(length * scale)
        turtle.left(outer_angle)
        turtle.forward(length * scale / (2 * math.cos(math.radians(inner_angle))))
        turtle.penup()
        turtle.backward(length * scale / (2 * math.cos(math.radians(inner_angle))))
        turtle.left(inner_angle)

turtle.speed(0)  # Set the drawing speed to maximum
draw_star(60, 5, 1)  # Adjust parameters as needed (length, sides, scale)
turtle.done()
