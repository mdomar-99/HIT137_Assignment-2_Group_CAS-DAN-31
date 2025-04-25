import turtle
import time

def draw_tree(length, left_angle, right_angle, depth, factor):
    if depth == 0:
        return
    turtle.forward(length)
    turtle.left(left_angle)
    draw_tree(length * factor, left_angle, right_angle, depth - 1, factor)
    turtle.right(left_angle + right_angle)
    draw_tree(length * factor, left_angle, right_angle, depth - 1, factor)
    turtle.left(right_angle)
    turtle.backward(length)

# Ask for user input
length = float(input("Enter starting branch length: "))
left_angle = float(input("Enter left branch angle: "))
right_angle = float(input("Enter right branch angle: "))
depth = int(input("Enter recursion depth: "))
factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

# Setup turtle screen
turtle.speed(0)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()

# Draw the tree
draw_tree(length, left_angle, right_angle, depth, factor)

# Hide turtle and hold window open
turtle.hideturtle()
turtle.done()