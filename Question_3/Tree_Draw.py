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

# Setup turtle screen
turtle.speed(0)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()

# Draw the tree
draw_tree(150, 30, 35, 8, 0.7)

# Hide turtle and hold window open
turtle.hideturtle()
turtle.done()
time.sleep(100)
